from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    #path('', views.home, name="home"),
    path('', views.home, name="home"),
    path('addNewList/', views.addNewList, name="addNewList"),
    path('deleteList/<int:list_id>/', views.deleteList, name="deleteList"),
    path('addNewItem/', views.addNewItem, name="addNewItem"),
    url(r'^ajax/displayItem/$', views.displayItem, name='displayItem'),  # index view at /
]