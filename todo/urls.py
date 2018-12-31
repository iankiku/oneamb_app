#dir = ./todo 
from . import views
from django.urls import path

from .views import All_Items

urlpatterns = [
    path('', views.All_Items, name='todo'),
    path('deleteItem/<todo_id>', views.deleteItem, name='delete'),
    path('<int:todo_id>/', views.detailView, name='detail'), 
    path('updateItem/<todo_id>/', views.updateItem, name='update'),       
]
