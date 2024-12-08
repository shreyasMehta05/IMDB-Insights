# Write a Python Program that allows user to filter the TV Shows based on:
# 1. Genre
#  2. IMDB rating
#  3. No. of episode
#  For each filter take user-input to choose the criteria. The user must be prompted a range
#  (inclusive of both the limits) for IMDB rating and No. of episode and Genre must be a
#  string input consisting of genres separated by spaces. Print the TV-show in the descending
#  order based on the user-filtering
import mysql.connector
import matplotlib.pyplot as plt

db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jee@1504",
        database="top_250_shows"
    )
cursor = db_connection.cursor()
useDatabaseQuery="USE top_250_shows"
cursor.execute(useDatabaseQuery)

cursor.execute("SELECT Genre FROM tv_shows")
result=cursor.fetchall()


genre=input("Enter the genres: ")
genre=genre.split()
genre=' '.join(genre)

ratingRange=input("Enter the rating range (a,b): ")
ratingRange=ratingRange.split()

ratingRange[0]=float(ratingRange[0])
ratingRange[1]=float(ratingRange[1])
episodeRange=input("Enter the episode range (a,b): ")
episodeRange=episodeRange.split()
episodeRange[0]=int(episodeRange[0])
episodeRange[1]=int(episodeRange[1])


if ratingRange[0]>ratingRange[1]:
    ratingRange[0],ratingRange[1]=ratingRange[1],ratingRange[0]
if episodeRange[0]>episodeRange[1]:
    episodeRange[0],episodeRange[1]=episodeRange[1],episodeRange[0]
    
query="SELECT * FROM tv_shows WHERE Genre LIKE %s AND Rating BETWEEN %s AND %s AND episodes BETWEEN %s AND %s ORDER BY Rating DESC"
cursor.execute(query,('%'+genre+'%',ratingRange[0],ratingRange[1],episodeRange[0],episodeRange[1]))
result=cursor.fetchall()
sum=0
print("---------------------------------------------------------------------------------------------------")
print("Matched Result: ")
print("------------------")
for row in result:
    print("\t",row[1],row[3],row[5])
    sum+=1
print("---------------------------------------------------------------------------------------------------")
print("Total Results: ",sum)
print("---------------------------------------------------------------------------------------------------")
cursor.close()