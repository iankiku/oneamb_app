#dir = ./tweetsbank 
from . import views
from django.urls import path


from .views import  TweetStream

urlpatterns = [
    path('', TweetStream.as_view(), name='home'),
    # path('', views.getTweets, name='home'),  
]
