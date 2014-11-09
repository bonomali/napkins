from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=5000)
    links = models.CharField(max_length=100)
    # position = models.ForeignKey('Plan', null=True, default=None)

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    profile = models.ForeignKey('Profile', null=True, default=None)

def upload_resume_to(instance, filename):
    import os
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'profiles/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )

class Profile(models.Model):
	github_url = models.CharField(max_length=50)
	linkedin_url = models.CharField(max_length=50)
	personal_site_url = models.CharField(max_length=50)

	phone = models.CharField(max_length=50)
	college = models.CharField(max_length=50)
	gpa = models.CharField(max_length=10)
	graduation_date = models.DateTimeField()

	resume = models.FileField(("Resume"), upload_to=upload_resume_to, blank=True)

class EmailList(models.Model):
    email = models.CharField(max_length=50)
    
