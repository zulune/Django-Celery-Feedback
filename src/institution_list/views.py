from django.shortcuts import render

from django.views.generic import ListView, DetailView

from feedback.forms import FeedbackForm
from .models import Institution
# Create your views here.

class InstitutionListView(ListView):
    template_name = 'institution_list/home_list.html'

    def get_queryset(self):
        return Institution.objects.all()

    def get_context_data(self, **kwargs):
        context = super(InstitutionListView, self).get_context_data(**kwargs)
        context['form'] = FeedbackForm()
        return context


class InstitutionDetailView(DetailView):
    template_name = 'institution_list/detail_view.html'

    def get_queryset(self):
        return Institution.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(InstitutionDetailView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        context['title'] = "{} Detail".format(name)
        context['form'] = FeedbackForm()
        return context
