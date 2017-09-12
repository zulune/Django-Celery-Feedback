from django import forms
from notification.tasks import send_notification_email_task

# Code here

class NotificationForm(forms.Form):
    subject         = forms.CharField()
    message         = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        print("Form complite")
        send_notification_email_task.delay(
            self.cleaned_data['subject'],
            self.cleaned_data['message']
        )
