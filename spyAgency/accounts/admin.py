from django.contrib import admin
from .models import HitMan, CustomUser, Manager

# Register your models here.
admin.site.register(HitMan)
admin.site.register(CustomUser)
admin.site.register(Manager)

