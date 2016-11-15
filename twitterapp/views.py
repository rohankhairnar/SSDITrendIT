import tweepy
from django.shortcuts import render
from twitterapp import config
import twitter
from tweepy.auth import OAuthHandler


auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_key,config.access_secret)

api = tweepy.API(auth)
trends_list = api.trends_place(config.us_trends)
# for t in trends_list[0]["trends"]:
#      trend_name=t['name']
#      print(t['name'])

import json
import simplejson

#print(json.dumps(trends_list, indent=1))
#print

trends_list_set = set([trend['name']
                     for trend in trends_list[0]['trends']])



list_trends = trends_list_set.intersection(trends_list_set)

#print(list_trends)
print(trends_list_set)

def index(request):
    json_list = trends_list_set
    context = {'json_list':json_list}
    return render(request, 'app/index.html', context)