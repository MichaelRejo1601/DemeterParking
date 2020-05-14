from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
# Create your views here.

def landing(request):
    context = {}
    return render(request, "index.html", context)

def register(response):
    if response.method == "POST":
        form =  UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
        else:
            context = {'form':form}
            return render(response, "register.html", context)
    else:
        form =  UserCreationForm()
        context = {'form':form}
        return render(response, "register.html", context)
