import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class KeyValue(models.Model):
    key = models.CharField(max_length=25,unique=True)
    value = models.CharField(max_length=100)
    timestamp = models.DateTimeField(
        default=timezone.now() + datetime.timedelta(minutes=5))

    def __str__(self):
        return self.key

