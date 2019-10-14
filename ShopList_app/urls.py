from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.home, name="home"),
    path('', views.home, name="home"),
    path('addNewList/', views.addNewList, name="addNewList"),
]