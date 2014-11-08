from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=5000)
    # position = models.ForeignKey('Plan', null=True, default=None)

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

class Profile(models.Model):
	github_url = models.CharField(max_length=50)
	linkedin_url = models.CharField(max_length=50)
	personal_site_url = models.CharField(max_length=50)

	
