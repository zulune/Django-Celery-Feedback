from django.conf.urls import url
from .views import InstitutionListView, InstitutionDetailView

urlpatterns = [
    url(r"^$", InstitutionListView.as_view(), name='list-view'),
    url(r"^(?P<slug>[-\w]+)/detail/$", InstitutionDetailView.as_view(), name='detail-view'),
]
