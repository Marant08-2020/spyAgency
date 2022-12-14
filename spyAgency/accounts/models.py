from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

STATE = (
    ('A', 'Active'),
    ('I', 'Inactive'),
)


# Create your models here.
class CustomUser(AbstractUser):
    is_boss = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_hitman = models.BooleanField(default=False)
    email = models.EmailField(_('email address'))

    def get_boss_profile(self):
        boss_profile = None
        if hasattr(self, 'boss'):
            boss_profile = self.boss
        return boss_profile

    def get_manager_profile(self):
        manager_profile = None
        if hasattr(self, 'manager'):
            manager_profile = self.manager
        return manager_profile

    def get_hitman_profile(self):
        hitman_profile = None
        if hasattr(self, 'hitman'):
            hitman_profile = self.hitman
        return hitman_profile

    class Meta:
        db_table = 'auth_user'


class Boss(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default='username')
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=1, choices=STATE)

    def __str__(self):
        return f'{self.user}'


class Manager(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default='username')
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=1, choices=STATE)

    def __str__(self):
        return f'{self.user}'


class HitMan(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default='username')
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=1, choices=STATE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True,
                                blank=True, default='username')

    def __str__(self):
        return f'{self.user}'
