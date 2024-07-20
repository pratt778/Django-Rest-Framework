from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [

    path('/list',carlist,name='carlist'),
    path('/<int:pk>',cardetails,name='cardetail')
]
