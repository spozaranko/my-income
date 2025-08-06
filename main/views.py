from django.contrib.admin.actions import delete_selected
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .serializer import WebUserSerializer
from rest_framework.response import Response
from .forms import LoginForm, SignUpform


def login(request):
    return render(request, 'registration/login.html')

def get_login_form(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

    return render(request, 'registration/login.html', {'form': form})

class Signup(APIView):
    def post(self, request):
        serializer = WebUserSerializer(data=request.data)
        if serializer.is_valid():
            user = WebUserSerializer.save()
            return Response({'user': user, "user created": user.username, "id":user.id})
        return Response({'error': serializer.errors})

def logout(request):
    return render(request, 'registration/logout.html')