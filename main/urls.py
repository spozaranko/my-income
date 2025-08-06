from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name = "login"),
    path("signup", views.Signup.as_view(), name = "signup")
]