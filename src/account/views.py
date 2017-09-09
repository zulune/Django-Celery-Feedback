from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import DetailView, CreateView

from account.forms import RegisterForm
from account.models import Profile
# Create your views here.

User = get_user_model()


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = '/'
    success_message = "Success registration! Thank you for a register in us site"

    def dispatch(self, *args, **kwargs):
        return super(RegisterView, self).dispatch(*args, **kwargs)


class ProfileView(DetailView):
    template_name = 'account/profile.html'

    def get_object(self):
        username = self.kwargs.get("username")
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        user = context['user']
        return context
