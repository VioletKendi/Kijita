from django.contrib.auth import authenticate, login, logout
from imaplib import _Authenticator
from pyexpat.errors import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from . forms import SignupForm
from django.urls import reverse

def index(request):
    return render(request, "kijita/index.html")

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login = (request, user)
            messages.success(request, ("Successful"))

    else:
        form = SignupForm()

    return render(request, "kijita/signup.html", {'form' : form})
    

    return render(request, "kijita/signup.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['password']
        user = authenticate(request, username= username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse, ("index"))
        else:
            return render(request, "kijita/login.html",
            {"message" : "Invalid Credentials"})
    else:
        return render(request, "kijita/login.html")