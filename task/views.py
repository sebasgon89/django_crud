from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def hello_world(request):
    return render(request, "signup.html",{
        'form':UserCreationForm
    })

