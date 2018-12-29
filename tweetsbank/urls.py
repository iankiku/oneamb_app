#dir = ./tweetsbank 

from django.urls import path

from .views import TweetsPageView

urlpatterns = [
    path('', TweetsPageView.as_view(), name='home'),
    
]
