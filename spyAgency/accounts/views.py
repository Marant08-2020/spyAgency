from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from .models import CustomUser
from .forms import MangerFormRegister, HitmanFormRegister, RegisterForm


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


def assignManager(request):

    users = CustomUser.objects.order_by('id')
    #users = users.values_list('id', 'username', 'email')
    return render(request, 'accounts/asingmanager.html', {'users': users})


class MangerRegister(CreateView):

    form_class = MangerFormRegister
    template_name = 'accounts/users_register.html'

    def form_valid(self, form):
        form.save()
        return redirect('/')


class HitManRegister(CreateView):

    form_class = HitmanFormRegister
    template_name = 'accounts/users_register.html'

    def form_valid(self, form):
        form.save()
        return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'accounts/registeruser.html'
    success_url = reverse_lazy('login')

