#dir = ./todo 
from . import views
from django.urls import path

from .views import All_Items

urlpatterns = [
    path('', views.All_Items, name='todo'),
    path('deleteItem/<todo_id>', views.deleteItem, name='delete'),

]
