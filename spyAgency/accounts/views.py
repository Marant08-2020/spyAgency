from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView

from .models import CustomUser, HitMan
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


def ListHitmenDetails(request):
    current_user = request.user

    if str(current_user) == "AnonymousUser":
        raise PermissionDenied
    if current_user.is_manager or current_user.is_boss:
        if current_user.get_manager_profile() or current_user.get_boss_profile():

            hitman = HitMan.objects.order_by('id')
        else:
            raise PermissionDenied
    else:
        raise PermissionDenied

    return render(request, 'accounts/listhitman.html', {'hitman': hitman})


def ListHitmenChange(request):
    current_user = request.user
    if str(current_user) == "AnonymousUser":
        raise PermissionDenied
    if current_user.is_boss:
        if current_user.get_boss_profile():

            hitman = HitMan.objects.order_by('id')
        else:
            raise PermissionDenied
    else:
        raise PermissionDenied

    return render(request, 'accounts/listhitmanedit.html', {'hitman': hitman})


def HitmanDetails(request, _id):
    current_user = request.user

    if str(current_user) == "AnonymousUser":
        raise PermissionDenied
    if current_user.is_manager or current_user.is_boss:
        if current_user.get_manager_profile() or current_user.get_boss_profile():

            hitman = HitMan.objects.get(pk=_id)
        else:
            raise PermissionDenied
    else:
        raise PermissionDenied

    return render(request, 'accounts/detailshitman.html', {'hitman': hitman})


class MangerRegister(CreateView):
    account = ''
    form_class = MangerFormRegister
    template_name = 'accounts/users_register.html'

    def form_valid(self, form):
        account = self.request.user
        form(user=self.request.user)
        if account.is_boss:
            roleB = account.get_boss_profile()
            if roleB:
                form.save()
                return redirect('/')
            else:
                return HttpResponseForbidden()
        else:
            return HttpResponseForbidden()
        return redirect('/')


class UpdateHitMan(UpdateView):
    model = HitMan
    form_class = HitmanFormRegister
    template_name = 'accounts/users_register.html'

    def form_valid(self, form):
        account = self.request.user

        if account.is_boss:
            roleB = account.get_boss_profile()
            if roleB:
                form.save()
                return redirect('/')
            else:
                return HttpResponseForbidden()
        else:
            return HttpResponseForbidden()
        return redirect('/')


class HitManRegister(CreateView):
    form_class = HitmanFormRegister
    template_name = 'accounts/users_register.html'

    def form_valid(self, form):
        account = self.request.user

        if account.is_boss:
            roleB = account.get_boss_profile()
            if roleB:
                form.save()
                return redirect('/')
            else:
                return HttpResponseForbidden()
        else:
            return HttpResponseForbidden()
        return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'accounts/registeruser.html'
    success_url = reverse_lazy('login')
