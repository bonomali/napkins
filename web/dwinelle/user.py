import jsonpickle

class UserPlain():
	def __init__(self, user):
		self.first_name = user.first_name
		self.last_name = user.last_name
		self.email = user.email
		self.github_url = user.profile.github_url
		self.linkedin_url = user.profile.linkedin_url
		self.personal_site_url = user.profile.personal_site_url
		self.phone = user.profile.phone
		self.college = user.profile.college
		self.gpa = user.profile.gpa
		self.graduation_date = user.profile.graduation_date
		self.resume = user.profile.resume.url

	def getField(string):
		if string == "full name":
			return self.first_name + " " + self.last_name

def UserToJson(user):
	return jsonpickle.encode(user)

def JsonToUser(json):
	return jsonpickle.decode(json)

