#dir = ./todo 
from . import views
from django.urls import path

from .views import All_Items, UpdateView

urlpatterns = [
    path('', views.All_Items, name='todo'),
    
    path('deleteItem/<todo_id>', views.deleteItem, name='delete'),

    path('<int:todo_id>/', views.detailView, name='detail'), 

    path('edit/<todo_id>', views.edit, name='edit'),     
    path('update/<id>', UpdateView.as_view(), name='update')  
]
