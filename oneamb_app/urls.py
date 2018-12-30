from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tweetsbank.urls')),
    path('todo/', include('todo.urls'))
    
]
