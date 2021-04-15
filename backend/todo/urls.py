from django.urls import path

from todo import views
  
urlpatterns = [          
    path('addTask/', views.AddTask().as_view(),name='addTask'),
    path("summary/", views.Summary().as_view(),name='summery'),
]