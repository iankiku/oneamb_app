from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

import tweepy
import twitter_config as config
# Create your views here.
# def tweetsPageView(request):
#     return HttpResponse('Hello, tweets bankers')
# print("...key: ", config.api_key)
class TweetsPageView(TemplateView):
    template_name = "home.html"


    def getUser(request):
        # import api keys
        auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
        # set api token
        auth.set_access_token(config.access_token, config.token_secret)
        # create object
        api = tweepy.API(auth)
        # ------------------------
        print ('user..')
        user = api.get_user('iankiku')
        for items in user:
            return (items)
        


