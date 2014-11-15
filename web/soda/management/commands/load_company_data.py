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
# company_list['palantir'] = {'name':'Palantir', 'description': 'Palantir Technologies, Inc. is an American computer software and services company, specializing in data analysis. Primary clients are the US government customers, and since 2010, financial customers.', 'links': 'https://www.selectleaders.com/employer/companylogo?download=1&eid=10545'}
company_list['affirm'] = {'name': 'Affirm', 'description' : 'Affirm lets shoppers pay for purchases across multiple months with transparent, fairly-priced fees built into every payment, and boosts conversion and basket size for eTailers at less than the cost of credit cards.','links': 'https://d1qb2nb5cznatu.cloudfront.net/startups/i/178430-585fa2c6225328beaedec4ce1ac8c924-medium_jpg.jpg?buster=1392918465'}
company_list['quora'] = {'name':'Quora','description':'Quora is a question-and-answer website where questions are created, answered, edited and organized by its community of users','links':'http://www.joshhannah.com/wp-content/uploads/quora-logo.png'}
company_list['box'] = {'name':'Box', 'description':"Box Inc. (formerly Box.net) is an online file sharing and personal cloud content management service for businesses. The company adopted a freemium business model, and provides up to 10 GB of free storage for personal accounts.", 'links':"http://8.mshcdn.com/wp-content/uploads/2009/02/box-logo-blue-background-300x181.png"}
company_list['arista'] = {'name':'Arista', "description":"Arista Networks (previously Arastra) is a computer networking company headquartered in Santa Clara, California, USA. The company designs and sells multilayer network switches to deliver software-defined networking (SDN) solutions for large datacenter, cloud computing, high-performance computing and high-frequency trading environments.", 'links':"http://media.glassdoor.com/sqll/295128/arista-networks-squarelogo.png"}
company_list['stripe'] = {'name':'Stripe', "description":"Stripe is a company that provides a way for individuals and businesses to accept payments over the Internet. Co-founded by brothers Patrick and John Collison, the company has received $130 million in funding.", 'links':"https://stripe.com/img/open-graph/logo.png?2"}
company_list['ea'] = {'name':'EA', 'description':"Electronic Arts, Inc. (EA), also known as EA Games, is an American developer, marketer, publisher and distributor of video games headquartered in Redwood City, California, U.S. Founded and incorporated on May 28, 1982 by Trip Hawkins, the company was a pioneer of the early home computer games industry and was notable for promoting the designers and programmers responsible for its games.", 'links':"https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQx6kyVodp_6YRGGH_myDzvvN5RMpSIBozUZH8mJjmombiYcIuT"}
company_list['mongodb'] = {'name':"MongoDB", 'description':"MongoDB is a cross-platform document-oriented database. Classified as a NoSQL database, MongoDB eschews the traditional table-based relational database structure in favor of JSON-like documents with dynamic schemas (MongoDB calls the format BSON), making the integration of data in certain types of applications easier and faster.", 'links':"https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTx6TxNovLD8X24W4HV8dbxBylmg8R_8KDeXVR63wEjyoyWe_kf"}
company_list['square'] = {'name':"Square", 'description':"Square, Inc. is a financial services, merchant services aggregator and mobile payments company based in San Francisco, California. The company markets several software and hardware products and services, including Square Register and Square Order. The company was founded in 2009 by Jack Dorsey and Jim McKelvey and launched its first app and service in 2010.", 'links':"https://pbs.twimg.com/profile_images/458796011356311552/2D5G8yIo.png"}
