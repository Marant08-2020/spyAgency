from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.forms import ModelForm

from .models import CustomUser, Manager, HitMan

STATE = (
    ('A', 'Active'),
    ('I', 'Inactive'),
)

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')


class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2')


class MangerFormRegister(ModelForm):

    is_manager = forms.BooleanField(required=True)

    class Meta:
        model = Manager
        fields = ('user', 'name', 'state')

    def save(self, commit=True):

        user = super().save(commit=False)
        if commit:
            user.save()
            userName = self.cleaned_data.get('user')
            userCustom = CustomUser.objects.get(username=userName)
            userCustom.is_manager = self.cleaned_data.get('is_manager')
            userCustom.save()
        return user


class HitmanFormRegister(ModelForm):
    is_hitman = forms.BooleanField(required=True)

    class Meta:
        model = HitMan
        fields = ('user', 'name', 'state', 'manager')

    def save(self, commit=True):

        user = super().save(commit=False)
        if commit:
            user.save()
            userName = self.cleaned_data.get('user')
            userCustom = CustomUser.objects.get(username=userName)
            userCustom.is_hitman = self.cleaned_data.get('is_hitman')
            userCustom.save()
        return user


