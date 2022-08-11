from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import CreateView

from .models import CustomUser
from .forms import MangerFormRegister, HitmanFormRegister


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('hits/')
            else:
                messages.error(request, "Invalid username or password")

        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'accounts/login.html', context={'form': AuthenticationForm()})


def register(request):
    return render(request, 'accounts/register.html')


class MangerRegister(CreateView):

    #model = CustomUser
    form_class = MangerFormRegister
    template_name = 'accounts/users_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/hits')


class HitManRegister(CreateView):

    #model = CustomUser
    form_class = HitmanFormRegister
    template_name = 'accounts/users_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/hits')


def logout_user(request):
    logout(request)
    return redirect('/')
