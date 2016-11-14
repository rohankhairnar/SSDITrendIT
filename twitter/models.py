from django.db import models
from django.contrib.auth.models import Group
#from twitter import forms
#from twitter import views
import tweepy
#from twitter import config

import sqlite3
from twitter import config


conn = sqlite3.connect('/Users/rohankhairnar/PycharmProjects/trenditapp/db.sqlite3')
print("Opened database successfully")
c = conn.cursor()

# Create your models here.
class trends(models.Model):
    #group = models.OneToOneField(Group)

    def Populate(self):
        auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
        auth.set_access_token(config.access_key, config.access_secret)
        api = tweepy.API(auth)

        trends_list = api.trends_place(1)
        c.execute("DELETE FROM auth_group")
        trend_id = 1

        for t in trends_list[0]["trends"]:
            trend_name = t['name']
            print(t['name'])
            c.execute("INSERT INTO auth_group VALUES (?, ?);", (trend_id, trend_name))
            trend_id = trend_id + 1


