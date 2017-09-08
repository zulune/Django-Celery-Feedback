from django.shortcuts import render
from django.views.generic import FormView

from .forms import FeedbackForm
# Create your views here.

class FeedbackView(FormView):
    template_name = 'feedback/contact.html'
    form_class = FeedbackForm
    success_url = '/'

    def form_valid(self, form):
        form.send_email()
        return super(FeedbackView, self).form_valid(form)
