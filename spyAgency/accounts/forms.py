from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

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

    def clean(self):
        super(MangerFormRegister, self).clean()
        account = self.user
        user = self.cleaned_data.get('user')
        if account == user:
            self._errors['user'] = self.error_class([
                'You can\'t assign yourself'])
        return self.cleaned_data

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

    def clean(self):
        user1 = self.cleaned_data.get('user')
        manager = self.cleaned_data.get('manager')
        if str(manager) == str(user1):
            self._errors['user'] = self.error_class([
                'You can\'t assign the same person like manager'])
        return self.cleaned_data


    def save(self, commit=True):


        user = super().save(commit=False)
        if commit:
            user.save()
            userName = self.cleaned_data.get('user')
            userCustom = CustomUser.objects.get(username=userName)
            userCustom.is_hitman = self.cleaned_data.get('is_hitman')
            userCustom.save()
        return user
