# scraping the data from the website and storing it in my database
# Assumption database exists
import urllib.request
import re
import mysql.connector
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import json

db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jee@1504",
        database="top_250_shows"
    )

cursor = db_connection.cursor()
cursor.execute("SHOW DATABASES LIKE 'top_250_shows'")

result= cursor.fetchone()
# Assuming database exists
if result is None:
    print("Database does not exist")
    exit()



url="https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
Req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
page=urllib.request.urlopen(Req)
soup=BeautifulSoup(page,'html.parser')
# ---------- Writing the content of the website to a file -----------
# --            For Reference only                        --
with open('index.html','w',encoding='utf-8') as file:
    file.write(str(soup))
# print(soup.prettify())

useDatabaseQuery="USE top_250_shows"

cursor.execute(useDatabaseQuery)
# if table exists drop previous one
cursor.execute("DROP TABLE IF EXISTS tv_shows")
cursor.execute("CREATE TABLE IF NOT EXISTS tv_shows (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), year INT, rating FLOAT, genre VARCHAR(255), episodes INT)")



# --------------------------  Scraping the data from the website and storing it in my database  --------------------------

    # ----- Extracting the title from the div tag and storing it in the database ----
divTags=soup.find_all('div',class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-be6f1408-9 srahg cli-title')
for divTag in divTags:
    h3Tag=divTag.find('h3',class_='ipc-title__text')
    if h3Tag:
        text=h3Tag.text.strip()
        dotSpaceIndex=text.find('. ')
        if dotSpaceIndex!=-1:
            strippedText=text[dotSpaceIndex+2:]
            insertQuery="INSERT INTO tv_shows (title) VALUES (%s)"
            cursor.execute(insertQuery,(strippedText,))
            print(strippedText)
            
spanTags=soup.find_all('span',class_='sc-be6f1408-8 fcCUPU cli-title-metadata-item')

pattern=r'\d+\s+eps'
    # ----- Extracting the number of episodes from the span tag and storing it in the database ---- 
showId=1
for spanTag in spanTags:
    text=spanTag.text.strip()
    match=re.search(pattern,text)
    if match:
        episodes=match.group(0).split()[0]
        updateQuery="UPDATE tv_shows SET episodes=%s WHERE id=%s"
        cursor.execute(updateQuery,(episodes,showId))
        showId+=1
        print(episodes)
        
    # ----- Extracting the rating from the span tag and storing it in the database ----
spanTags=soup.find_all('span',class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating')
showId=1
for spanTag in spanTags:
    spanText=spanTag.text.strip()
    firstWord=spanText.split()[0]
    rating=float(firstWord)
    updateQuery="UPDATE tv_shows SET rating=%s WHERE id=%s"
    cursor.execute(updateQuery,(rating,showId))
    showId+=1
    print(rating)

    #  ----- Extracting the genre from the script tag and storing it in the database ----
scriptTag=soup.find('script',id='__NEXT_DATA__')
if scriptTag:
    scriptContent=scriptTag.string
    if scriptContent:
        data=json.loads(scriptContent)
        chartTitlesEdges=data['props']['pageProps']['pageData']['chartTitles']['edges']
        showId=1
        for edge in chartTitlesEdges:
            titleGenresData=edge['node']['titleGenres']['genres']
            genresString=' '.join(genre['genre']['text'] for genre in titleGenresData)
            updateQuery="UPDATE tv_shows SET genre=%s WHERE id=%s"
            cursor.execute(updateQuery,(genresString,showId))
            print(genresString)
            showId+=1

  # ----- Extracting the year from the span tag and storing it in the database ----  
divTags = soup.find_all('div', class_='sc-be6f1408-7 iUtHEN cli-title-metadata')
# <div class="sc-be6f1408-7 iUtHEN cli-title-metadata"><span class="sc-be6f1408-8 fcCUPU cli-title-metadata-item">2008–2013</span><span class="sc-be6f1408-8 fcCUPU cli-title-metadata-item">62 eps</span><span class="sc-be6f1408-8 fcCUPU cli-title-metadata-item">18</span></div>
showId = 1
for divTag in divTags:
    span = divTag.find('span', class_='sc-be6f1408-8 fcCUPU cli-title-metadata-item')
    if span:
        text = span.text.strip()
        year = text.split('–')[0]
        updateQuery = "UPDATE tv_shows SET year=%s WHERE id=%s"
        cursor.execute(updateQuery, (year, showId))
        showId += 1
        print(year)

#  A bar graph representing Genre (on x-axis) to no. of TV-shows belonging to that genre
#  (on y-axis). (Note: A TV Show might have multiple genre)
#  ii.
# A line graph representing the frequency count of TV-shows having n episodes, n varies
#  from 1 to maximum no. of episodes present. Represent no. of episodes (on x-axis) and
#  frequency count (on y-axis)
# -------------------------- Visualizing the data  --------------------------------

# ------------------ part 1 ---------------------
part1="SELECT genre FROM tv_shows"
cursor.execute(part1)

genreDict={}
for row in cursor.fetchall():
    temp_list=row[0].split()
    for genre in temp_list:
        if genre in genreDict:
            genreDict[genre]+=1
        else:
            genreDict[genre]=1
genreItem=genreDict.keys()
genreCount=genreDict.values()


plt.bar(genreItem,genreCount, color='skyblue', edgecolor='black', alpha=0.7)
plt.xticks(rotation=40)
plt.xlabel('Genre',fontsize=1)
plt.ylabel('Number of shows')
plt.title('Genre vs Number of shows')
plt.show()

# ------------------ part 2 ---------------------   
part2="SELECT episodes FROM tv_shows"
cursor.execute(part2)
episodesList=[row[0] for row in cursor.fetchall()]
maxEpisodes=max(episodesList)
minEpisodes=min(episodesList)
episodeList=[]
for i in range(minEpisodes, maxEpisodes+1):
    cursor.execute("SELECT COUNT(*) FROM tv_shows WHERE episodes = %s", (i,))
    result = cursor.fetchone()
    episodeList.append(result[0])
plt.figure(figsize=(10, 6))
plt.grid(True)


# Generating a list of non-zero episodes and their counts for plotting
nonZeroEpisodes = [count for count in episodeList if count > 0]
nonZeroNumbersForPlot = [episode_number for episode_number, count in enumerate(episodeList, start=minEpisodes) if count > 0]

# --------- Plotting the graph ------------
# plt.plot(range(minEpisodes, maxEpisodes+1), episodeList, color='orange', marker='o')
plt.plot(nonZeroNumbersForPlot, nonZeroEpisodes, color='orange', marker='o')
plt.title('Episodes vs Number of shows')
plt.xlabel('Episodes')
plt.ylabel('Number of shows')
plt.xscale('log')
plt.show()

db_connection.commit()
cursor.close()