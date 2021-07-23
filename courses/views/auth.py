
from django.shortcuts import render, redirect
from django.views import View
from ..forms import RegistrationForm, LoginForm
from django.contrib.auth import logout

class Login(View):

    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(request, 'courses/login.html', context)

    def post(self, request):
        form = LoginForm(request,data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            return redirect('home')
        context = {'form': form}
        return render(request, 'courses/login.html', context)


def signout(request):
    logout(request)
    return redirect('login')

class Signup(View):

    def get(self, request):
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'courses/signup.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                return redirect('login')
        print(request.POST)
        context = {'form': form}
        return render(request, 'courses/signup.html', context)
