from django.conf import settings
from django.core.mail import EmailMessage, send_mass_mail
from django.template import Context
from django.template.loader import render_to_string


def send_notification_email(subject, message):
    c = Context({'subject': subject, 'message': message})
    email_subject = subject
    email_body = message
    from_email = settings.DEFAULT_FROM_EMAIL
    email = (
        email_subject, email_body,
        [from_email], ['mars.xaker@gmail.com']
    )
    print(email)
