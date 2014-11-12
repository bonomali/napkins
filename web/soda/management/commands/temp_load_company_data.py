#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from soda.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        for key in company_list.keys():
            company_dict = company_list[key]
            name = company_dict['name']
            company = Company.objects.filter(name=name)
            if company:
                company = company[0]
                company.description = company_dict['description']
                company.links = company_dict['links']
            else:
                company = Company(name=company_dict['name'], description=company_dict['description'], links=company_dict['links'])
            company.save()
        print str(len(Company.objects.all())) + " company data has been inserted."

company_list = {}
company_list['counsyl'] = {'name':'Counsyl', "description":"Counsyl is a technology company that strives to give millions of men and women access to vital information about their bodies so they can confidently make choices about their lives. Counsyl integrates sophisticated technology with custom automation in its CLIA-certified, CAP-accredited and NYS CLEP-permitted medical laboratory.", 'links':"http://counsyl.files.wordpress.com/2014/04/github-logo2.png"}
company_list['palantir'] = {'name':'Palantir', 'description': 'Palantir Technologies, Inc. is an American computer software and services company, specializing in data analysis. Primary clients are the US government customers, and since 2010, financial customers.', 'links': 'https://www.selectleaders.com/employer/companylogo?download=1&eid=10545'}
company_list['affirm'] = {'name': 'Affirm', 'description' : 'Affirm lets shoppers pay for purchases across multiple months with transparent, fairly-priced fees built into every payment, and boosts conversion and basket size for eTailers at less than the cost of credit cards.','links': 'https://d1qb2nb5cznatu.cloudfront.net/startups/i/178430-585fa2c6225328beaedec4ce1ac8c924-medium_jpg.jpg?buster=1392918465'}
company_list['quora'] = {'name':'Quora','description':'Quora is a question-and-answer website where questions are created, answered, edited and organized by its community of users','links':'http://www.joshhannah.com/wp-content/uploads/quora-logo.png'}
company_list['box'] = {'name':'Box', 'description':"Box Inc. (formerly Box.net) is an online file sharing and personal cloud content management service for businesses. The company adopted a freemium business model, and provides up to 10 GB of free storage for personal accounts.", 'links':"http://8.mshcdn.com/wp-content/uploads/2009/02/box-logo-blue-background-300x181.png"}