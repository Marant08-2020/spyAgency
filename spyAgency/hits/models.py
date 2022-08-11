from django.db import models
from accounts.models import HitMan


# Create your models here.
class Hits(models.Model):
    STATUS_STATE = (
        ('O', 'Open'),
        ('F', 'Failed'),
        ('C', 'Completed'),
    )

    description = models.CharField(max_length=255)
    target = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=STATUS_STATE)
    created_by = models.CharField(max_length=255, null=True,
                                  blank=True)
    id_hitman = models.ForeignKey(HitMan, on_delete=models.CASCADE, null=True,
                                  blank=True)

    def __str__(self):
        return f' Target:{self.target} Status:{self.status}'
