from django.core.management.base import BaseCommand, CommandError
from soda.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        companies = Company.objects.all()
        if companies:
        	print "there is already company data. failed."
        	return
        for key in short_list.keys():
            company_dict = short_list[key]
            company = Company(name=company_dict['name'], description=company_dict['description'])
            company.save()
        print str(len(Company.objects.all())) + " company data has been inserted."

short_list = {}
short_list['twilio'] = {'name': 'Twilio', 'description':"Twilio is a cloud communications (IaaS) company based in San Francisco, California. Twilio allows software developers to programmatically make and receive phone calls and send and receive text messages using its web service APIs. Twilio's services are accessed over HTTP and are billed based on usage."}
short_list['counsyl'] = {'name':'Counsyl', 'description':"Counsyl is a technology company that strives to give millions of men and women access to vital information about their bodies so they can confidently make choices about their lives. Counsyl integrates sophisticated technology with custom automation in its CLIA-certified, CAP-accredited and NYS CLEP-permitted medical laboratory. The Counsyl Family Prep Screen has already helped hundreds of thousands of people discover critical information before having children, and the Counsyl platform now includes inherited cancer screening."}