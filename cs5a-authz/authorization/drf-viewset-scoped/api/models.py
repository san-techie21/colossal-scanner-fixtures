from django.conf import settings
from django.db import models


class Statement(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=12, decimal_places=2)
