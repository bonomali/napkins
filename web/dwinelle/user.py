import jsonpickle
import urllib
import uuid
import pyPdf
import os
import string

class UserPlain():

	def __init__(self, user=None):
		if user:
			self.first_name = user.first_name
			self.last_name = user.last_name
			self.email = user.email
			self.github_url = user.profile.github_url
			self.linkedin_url = user.profile.linkedin_url
			self.personal_site_url = user.profile.personal_site_url
			self.phone = user.profile.phone
			self.college = user.profile.college
			self.gpa = user.profile.gpa
			self.resume_url = user.profile.resume.url
			self.address = user.profile.address
			self.city = user.profile.city
			self.state = user.profile.state
			self.zipcode = user.profile.zipcode
			self.major = "cs"
			self.coverletter = user.profile.coverletter

	def getResume(self):
		url = self.resume_url
		testfile = urllib.URLopener()
		filecode = "media/" + str(uuid.uuid4()) + ".pdf"
		testfile.retrieve(url, filecode)
		self.resume = filecode

	def resumeToText(self):
		pdf = pyPdf.PdfFileReader(open(self.resume, "rb"))
		content = ""
		for page in pdf.pages:
			content += page.extractText()
			content += " "
		content = content.replace('\n', ' ').replace('"', " ").replace("'", ' ')
		content = filter(lambda x: x in string.printable, content)
		return content

	def deleteResume(self):
		os.remove(self.resume)

	def getField(self, num, company=None):
		if num == 1.1:
			return self.first_name
		elif num == 1.2:
			return self.last_name
		elif num == 1:
			return self.first_name + " " + self.last_name
		elif num == 2:
			return self.email
		elif num == 3:
			return self.phone
		elif num == 4:
			return self.college
		elif num == 5:
			return self.gpa
		elif num == 6:
			return self.resume
		elif num == 7:
			return self.address
		elif num == 8:
			return self.city
		elif num == 9:
			return self.zipcode
		elif num == 9.1:
			return self.state
		elif num == 10:
			return self.major
		elif num == 11:
			return self.resumeToText()
		elif num == 12:
			return self.github_url
		elif num == 13:
			return self.linkedin_url
		elif num == 14:
			return self.personal_site_url
		elif num == 15:
			return self.coverletter.replace("[company]", company.name)

def UserToJson(user):
	return jsonpickle.encode(user)

def JsonToUser(json):
	return jsonpickle.decode(json)
