import tweepy
import random
from django.shortcuts import render
from twitterapp import config
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
import twitter
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import json
import simplejson

#for instagram
#from instagram.client import InstagramAPI

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_key,config.access_secret)

api = tweepy.API(auth)
# user_term = "trump"
# trendresults  =tweepy.Cursor(api.search, q=user_term).items(15)
# for i in trendresults:
#     print(i.text.encode("utf-8"))

#
# for k in trendresults:
#     print(k.text)
#neha = set([i.text.encode("utf-8") for i in trendresults])

#
# class MyListener(StreamListener):
#     def on_data(self, data):
#         try:
#             with open('python.json', 'a') as f:
#                 f.write(data)
#                 print(data)
#                 return True
#         except BaseException as e:
#             print(e)
#         return True
#
#     def on_error(self, status):
#             print(status)
#             return True
#
#

trends_list = api.trends_place(config.us_trends)
# for t in trends_list[0]["trends"]:
#      trend_name=t['name']
#      print(t['name'])

trends_list_set = set([trend['name']
                     for trend in trends_list[0]['trends']])



list_trends = trends_list_set.intersection(trends_list_set)

# #print(list_trends)
# print(trends_list_set)
# # twitter_stream = Stream(auth, MyListener())
# tweets = twitter_stream.filter(track=['#trump'])
# text = set([tweet['text']] for tweet in tweets[0]['tweets'])
# #for tweet in tweets:
# #    text = tweet["text"]
# print(text)
#
def index(request):
    json_list = trends_list_set
    surprise_term = random.choice(list(json_list))
    context = {'json_list':json_list,'surprise_term':surprise_term}
    return render(request, 'app/index.html', context)

def trend_results(request):
    if request.method=='GET':
            user_term = request.GET.get('searchterm')

        #if request.GET.get('search') == '#' and user_term is not None:
            print(user_term)
            trendresults = tweepy.Cursor(api.search, q=user_term).items(30)
            results = set([i.text.encode("utf-8") for i in trendresults])
            context = {'results':results,'searchterm':user_term}
            return render(request, 'app/results.html', context)
        # elif request.GET.get('search') == '#' and user_term is None:
        #     return HttpResponse("Enter a valid search term")
        # elif request.GET.get('surpriseme') == '!' and user_term is None:
        #     trendresults = tweepy.Cursor(api.search, q=random.choice(trends_list_set)).items(30)
        #     results = set([i.text.encode("utf-8") for i in trendresults])
        #     context = {'results': results, 'searchterm': user_term}
        #     return render(request, 'app/results.html', context)
        # else:
        #     return HttpResponse("Invalid entry")



# iapi = InstagramAPI(access_token="4198713157.1677ed0.a87376529a4b477fb872e4406dd9b3",client_secret="218732d700f443af9078892320565a06")
# user_tag = "trump"
#
#
# def insta_results(request):
#     user_tag = request.GET.get('searchterm')
#     content = "<h2>Tag Search</h2>"
#     #access_token = request.session['access_token']
#     #atag_search = iapi.tag_recent_media(tag_name=user_tag)
#     tag_search, next_tag = iapi.tag_search(q=user_tag)
#     tag_recent_media, next = iapi.tag_recent_media(tag_name=tag_search[0].name)
#     photos = []
#     for tag_media in tag_recent_media:
#         photos.append('<img src="%s"/>' % tag_media.get_standard_resolution_url())
#     content += ''.join(photos)
#     #photos = tag_search.
#     context = {'photos':content}
#     return render(request, 'app/results.html',context)

