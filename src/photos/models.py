from django.db import models

# Create your models here.
class Photo(models.Model):
    timestamp   = models.DateTimeField("Create on", auto_now_add=True)
    update      = models.DateTimeField("Update on", auto_now=True)
    title       = models.CharField("Title", max_length=100)
    link        = models.URLField("Photo link",
        max_length=255, help_text="The URL to the image page")
    image_url   = models.URLField("ImageURL",
        max_length=255, help_text="he URL to the image file itself")
    description = models.TextField("Description")

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
        ordering = ['-timestamp', 'title']

    def __str__(self):
        return self.title
