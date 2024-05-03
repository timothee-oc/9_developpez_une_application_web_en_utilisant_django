from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import View
from .forms import SignupForm

class Signup(View):
    template_name = "authentication/login.html"
    form_class = SignupForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
        return render(request, self.template_name, {'form': form})
