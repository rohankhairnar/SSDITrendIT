#from twitter.models import *
import tweepy
#from django.shortcuts import render
import sqlite3
from twitter import config
#from twitter import models


conn = sqlite3.connect('/Users/rohankhairnar/PycharmProjects/trenditapp/db.sqlite3')

print("Opened database successfully")

c = conn.cursor()


conn.commit()

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_key,config.access_secret)
api = tweepy.API(auth)

tweet_list = tweepy.Cursor(api.search, q="hillary").items(15)
for t in tweet_list:
    print(t.text)

trends_list = api.trends_place(1)
c.execute("DELETE FROM TRENDS")
trend_id=1
for t in trends_list[0]["trends"]:
    trend_name=t['name']
    print(t['name'])
    c.execute("INSERT INTO TRENDS VALUES (?, ?);", (trend_id, trend_name))
    trend_id = trend_id+1

list1 = c.execute("SELECT TRENDS.id FROM TRENDS")
print(list1)
conn.commit()
#
# def trendsview(request):
#     trend_name = trends.objects.get(id=1)
#     rohan = trend_name.name
#
#     return render(request,'/details',trend_name)


cursor = conn.execute("SELECT id from TRENDS LIMIT 20")
for row in cursor:
     print(row[0])