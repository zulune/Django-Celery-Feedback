from django.conf.urls import url

from .views import NotificationView

urlpatterns = [
    url(r'^send/$', NotificationView.as_view(), name="send"),
]
