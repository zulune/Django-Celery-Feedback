from django.shortcuts import render
from django.views.generic import ListView

from photos.models import Photo
from feedback.forms import FeedbackForm
# Create your views here.

class PhotoView(ListView):
    template_name = "photos/photo_list.html"
    paginate_by = 24

    def get_queryset(self):
        return Photo.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PhotoView, self).get_context_data(**kwargs)
        context['form'] = FeedbackForm()
        return context
