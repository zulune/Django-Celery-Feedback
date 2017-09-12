from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView

from .forms import NotificationForm
from feedback.forms import FeedbackForm
# Create your views here.


class NotificationView(SuccessMessageMixin, FormView):
    template_name = 'notification/note-form.html'
    form_class = NotificationForm
    success_url = "/"
    success_message = "Success sending email"

    def form_valid(self, form):
        form.send_email()
        return super(NotificationView, self).form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super(NotificationView, self).get_context_data(**kwargs)
    #     context['form'] = FeedbackForm()
    #     return context
