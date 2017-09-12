from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from .views import ProfileView, RegisterView, SubscribeView

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^subscribe-toggle/$', SubscribeView.as_view(), name="subscribe"),
    url(r'^(?P<username>[\w-]+)/$', ProfileView.as_view(), name="profile"),
]
