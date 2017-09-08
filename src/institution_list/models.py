from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save

from django.core.urlresolvers import reverse

from .utils import unique_slug_generator
# Create your models here.

class Institution(models.Model):
    name        = models.CharField(max_length=150)
    slug        = models.SlugField(blank=True, null=True, unique=True)
    description = models.TextField(blank=True, null=True)
    open_time   = models.TimeField(blank=True, null=True)
    close_time  = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('institution:detail-view', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.name


def i_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(i_pre_save_receiver, sender=Institution)
