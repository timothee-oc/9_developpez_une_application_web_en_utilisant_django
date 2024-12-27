from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms


def signup(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
    return render(request, "authentication/signup.html", {"form": form})


def log_in(request):
    form = forms.LoginForm()
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user:
                login(request, user)
                return redirect("feed")
    return render(request, "authentication/login.html", {'form': form})


def log_out(request):
    logout(request)
    return redirect("login")
