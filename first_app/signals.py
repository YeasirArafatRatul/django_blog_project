from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Person, PersonsProfile



# signal.py
@receiver(post_save, sender=Person)
def create_profile(sender, instance, created, **kwargs):
    if created:
        PersonsProfile.objects.create(user=instance)
        post_save.connect(create_profile, sender=Person)


from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
        post_save.connect(create_token, sender=User)



