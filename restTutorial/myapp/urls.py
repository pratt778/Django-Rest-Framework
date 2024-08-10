from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [

    path('/list',carlist,name='carlist'),
    path('/<int:pk>',cardetails,name='cardetail'),
    path('/showroom',ShowroomView.as_view(),name='showroom'),
    path('/showroom/<int:pk>',Showroomdetail.as_view(),name="showroomdetail"),
    path('/review',ReviewView.as_view(),name='reviews'),
    path('/review/<int:pk>',ReviewDetail.as_view(),name='revdetail'),
    
]
