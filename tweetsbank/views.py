from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView, ListView


import tweepy
import twitter_config as config


class TweetStream(TemplateView, tweepy.StreamListener):
    template_name = "home.html"

    # import api keys
    auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
    # set api token
    auth.set_access_token(config.access_token, config.token_secret)

    # create object
    api = tweepy.API(auth)

    def getStatus(self):
        pass
    

    def getTweetbyTag(self):
        pass

    def tweetsArchiver(self):
        pass











# def getTweets(request):
#     # import api keys
#     auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
#     # set api token
#     auth.set_access_token(config.access_token, config.token_secret)

#     # create object
#     api = tweepy.API(auth)
#     # ------------------------

#     print ('user..')
#     acc = api.get_user('iankiku')
#     print (acc.id)
#     mytweets = api.home_timeline()
#     # for items in user:
#     #     return (items)
#     return render(request, 'home.html', {'mytweets': mytweets})