
# backend/urls.py

from django.contrib import admin
from django.urls import path, include  

from rest_framework import routers                    
from todo import views                            
        
router = routers.DefaultRouter()                      
router.register(r'todos', views.TodoView, 'todo')    


        
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),           
    path('api/', include(router.urls),name='api'),
    path('test/', include('todo.urls')),      
]