from __future__ import division
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from soda.models import *

def email_send(subject, message, to_email, from_email=settings.QURSE_EMAIL, attachment=None):
	e = EmailMessage(subject, message, from_email, to_email)
	if attachment:
		f = open(attachment)
		e.attach("resume.pdf", f.read(), 'application/pdf')
	e.send()
