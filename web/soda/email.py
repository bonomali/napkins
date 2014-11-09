from __future__ import division
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from soda.models import *

def email_send(subject, message, to_email, from_email=settings.QURSE_EMAIL):
	send_mail(subject, message, from_email,
    to_email, fail_silently=False)

def company_app_data_email(email):
	companies = Company.objects.all()
	message = "Hello,\nHere is the data:\n\n"
	for company in companies:
		message += company.name
		message += "\t"
		message += company.links
		message += "\n"
	message += "\n\nBest,\nTroll Face"
	email_send("Software Engineer Internship App Data", message, [email])
