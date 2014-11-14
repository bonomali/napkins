from __future__ import division
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from soda.models import *

def email_send(subject, message, to_email, from_email=settings.QURSE_EMAIL):
	send_mail(subject, message, from_email,
    to_email, fail_silently=False)
