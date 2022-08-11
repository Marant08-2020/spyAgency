from django.forms import ModelForm
from django import forms

from .models import Hits

STATUS_STATE = (
    ('O', 'Open'),
    ('F', 'Failed'),
    ('C', 'Completed'),
)


class HitForm(ModelForm):

    class Meta:
        model = Hits
        fields = ['id_hitman', 'description', 'target', 'status']
