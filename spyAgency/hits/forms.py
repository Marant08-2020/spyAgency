from django.forms import ModelForm

from .models import Hits


class HitForm(ModelForm):
    class Meta:
        model = Hits
        fields = ['id_hitman', 'description', 'target', 'status']
