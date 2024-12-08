#  Create a word cloud of the above filtered TV Show list. The relative size of the
#  word in the word cloud will depend on the above priority order i.e. TV Show name on top
#  of the list should be printed with larger font-size
import mysql.connector
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image

db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jee@1504",
        database="top_250_shows"
    )
cursor = db_connection.cursor()
useDatabaseQuery="USE top_250_shows"
cursor.execute(useDatabaseQuery)

# table name: tv_shows
# generate a list of tv shows of title 
title=[]

cursor.execute("SELECT title FROM tv_shows")
result=cursor.fetchall()
for row in result:
    title.append(row[0])
# print(title)


mask = np.array(Image.open('mask.png')) 
weights= {word: len(title) - i for i, word in enumerate(title)}
wordcloud=WordCloud(width=1920, height=1080, background_color='black', max_words=350, mask=mask, contour_width=3, contour_color='gray').generate_from_frequencies(weights)
plt.figure(figsize=(8,8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()
cursor.close()

