from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import CustomUser, Manager, HitMan

STATE = (
    ('A', 'Active'),
    ('I', 'Inactive'),
)

m = Manager.objects.values_list('id').order_by('id')
m = list(m)
t = tuple([(int(x[0]), list(Manager.objects.filter(id=x[0]).values('name'))[0]['name']) for x in m])


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')


class MangerFormRegister(UserCreationForm):

    name = forms.CharField(required=True)
    state = forms.ChoiceField(required=True, choices=STATE)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2', 'is_manager')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        if commit:
            user.save()
            manager = Manager.objects.create(user=user)
            manager.name = self.cleaned_data.get('name')
            manager.state = self.cleaned_data.get('state')
            manager.save()
        return user


class HitmanFormRegister(UserCreationForm):

    name = forms.CharField(required=True)
    state = forms.ChoiceField(required=True, choices=STATE)
    manager = forms.TypedChoiceField(required=True, choices=t, coerce=int)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2', 'is_hitman')

    def save(self, commit=True):
        # Save the provided password in hashed format

        user = super().save(commit=False)
        if commit:
            user.save()
            hitman = HitMan.objects.create(user=user)
            hitman.name = self.cleaned_data.get('name')
            hitman.state = self.cleaned_data.get('state')
            _id = self.cleaned_data.get('manager')
            hitman.manager = Manager.objects.get(id=_id)
            hitman.save()
        return user


