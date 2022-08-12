from django.contrib import admin
from .models import HitMan, CustomUser, Manager, Boss

# Register your models here.
admin.site.register(HitMan)
admin.site.register(CustomUser)
admin.site.register(Manager)
admin.site.register(Boss)

