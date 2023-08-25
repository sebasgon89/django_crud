from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {
            'form': UserCreationForm
        })
    else:
        try:
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect("tasks")
        except:
            return render(request, "signup.html", {
                'form': UserCreationForm,
                'error': 'User already exists'
            })
    return render(request, "signup.html", {
        'form': UserCreationForm,
        'error': 'Passwords do not match'
    })


def tasks(request):
    return render(request, "tasks.html")