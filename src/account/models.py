from django.db import models
from django.db.models.signals import post_save

from django.conf import settings
from django.core.urlresolvers import reverse

from django.dispatch import receiver
# Create your models here.

User = settings.AUTH_USER_MODEL

class ProfileManager(models.Manager):
    def subscribe_toggle(self, request_user, notification):
        profile_ = Profile.objects.get(user=request_user)
        if notification:
            profile_.notification = False
        else:
            profile_.notification = True
        profile_.save()
        return profile_


class Profile(models.Model):
    user         = models.OneToOneField(User)
    timestamp    = models.DateTimeField(auto_now_add=True)
    update       = models.DateTimeField(auto_now=True)
    notification = models.BooleanField(default=True)

    objects = ProfileManager()

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
