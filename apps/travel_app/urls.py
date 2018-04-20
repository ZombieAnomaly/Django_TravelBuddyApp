from django.contrib import admin
from django.urls import path,re_path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register),
    path('home/', views.home),
    path('new/', views.new),
    path('new/add/', views.add),
    re_path('^home/destination/(?P<destination_id>\d+)/$', views.destination),
    re_path('^home/join/(?P<trip_id>\d+)/$', views.join),
]
