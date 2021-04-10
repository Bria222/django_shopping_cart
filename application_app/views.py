from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import *
def index(request):
    dataa= Details.objects.all()
    return render(request, 'application_app/index.html', {'dataa':dataa})

def register(request):
    return render(request, 'application_app/register.html')

    
       