from django.contrib.admin.actions import delete_selected
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpform


def login(request):
    return render(request, 'registration/login.html')

def get_login_form(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

    return render(request, 'registration/login.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpform()

    return render(request, 'registration/signup.html', {'form': form})


def logout(request):
    return render(request, 'registration/logout.html')