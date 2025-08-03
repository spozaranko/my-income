from django.urls import path
from . import views

urlpatterns = [
    path('', views.userpage, name = "userstats"),
    path('insertop', views.insertop, name = "insertop")
]