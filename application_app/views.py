from django.shortcuts import render
from .models import *
def index(request):
    dataa= Details.objects.all()
    return render(request, 'application_app/index.html', {'dataa':dataa})

def register(request):
    if request.method == 'post':
        first_name = request.post['first_name']


    else:
        return render(request, 'application_app/register.html')