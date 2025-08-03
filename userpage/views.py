from django.shortcuts import render
from .models import Operations


def userpage(request):
    operations = Operations.objects.all()
    return render(request, 'userpage/userstats.html',{'operations':operations})

def insertop(request):
    return render(request, 'userpage/insertop.html')