from splinter.browser import Browser
from pyvirtualdisplay import Display 
import time
import os
from soda.email import email_send

class Form:
	def __init__(self,url, name):
		self.name = name
		self.url = url
		self.html_button_clicks = [] #Click we have to do before filling forms
		self.Attach_Fields = {}
		self.Fill_Fields = {}
		self.Drop_Down_Fields = {}
		self.Drop_Down_Fields_Helper = {}
		self.CheckBoxes = []
		self.extraJavaScript = []
		self.extraJSHelper = {}
		self.finalSubmit = None
		self.email = {}
		self.submitJS = []
		self.greenHouseResume = False
	def hasGreenHouseResume(self):
		self.greenHouseResume = True
	def addEmail(self,em):
		self.email = em
	def addClicks(self, button_name):
		self.html_button_clicks.append(button_name)
	def addFillField(self, html_ele, field_num, name):
		self.Fill_Fields[html_ele] = (field_num, name)
	def addAttachField(self,html_ele, field_num):
		self.Attach_Fields[html_ele] = field_num
	def addDropDownField(self,html_ele,index):
		self.Drop_Down_Fields[html_ele] = index
	def addDropDownFieldHelper(self,html_ele,index):
		self.Drop_Down_Fields_Helper[html_ele] = index
	def addJSHelper(self,html_ele,index): 
		self.extraJSHelper[html_ele] = index
	def addCheckBox(self, html_ele):
		self.CheckBoxes.append(html_ele)
	def addJavaScript(self,java):
		self.extraJavaScript.append(java)
	def setFinalSubmit(self,val):
		self.finalSubmit = val
	def setSubmitJS(self,java):
		self.submitJS.append(java)

def emailFill(user,form):
	return "Hello " + form.email["name"] +",\nMy name is " + user.getField(1)  +  " and I am currently a student at " + user.getField(4) + ". I am applying for the Software Engineering Internship position for summer 2015. I can be reached at " + user.getField(2) + " or " + user.getField(3)+ ".\
		\nBest,\n" + user.getField(1)

def form_fill(user, form):
	# display = Display(visible=0, size=(800, 600))
	# display.start()
	if form.email != {}:
		st = emailFill(user, form)
		email_send("Software Internship Application",st,[form.email['email'], user.getField(2)],attachment=user.getField(6))
		return
	browser = Browser()
	browser.visit(form.url)
	if form.greenHouseResume:
		string = """$("#application_form").append('<input type="hidden" id="resume_url" name="job_application[resume_url]" value=""" + '"' + user.getField(6.1) + '"' + """><input type="hidden" id="resume_url_filename" name="job_application[resume_url_filename]" value="resume.pdf">')"""
		browser.execute_script(string)
	def doClicks(): #partial_htmls being dealt with
		for ele in form.html_button_clicks:
			browser.find_link_by_partial_href(ele)[0].click()
	def fillField():
		for ele, tple in form.Fill_Fields.iteritems():
			browser.fill(ele,user.getField(tple[0]))
	def attachField():
		for ele, field in form.Attach_Fields.iteritems():
			browser.attach_file(ele,os.getcwd() + "/" + user.getField(field))
	def dropDownField():
		for ele, index in form.Drop_Down_Fields.iteritems():
			browser.execute_script('document.getElementById("' + ele + '")[' + str(index) + '].selected=true')
	def dropDownHelper():
		for ele,index in form.Drop_Down_Fields_Helper.iteritems():
			browser.execute_script('document.getElementsByTagName("'+ele+'")['+str(index)+'].selected=true')
	def checkBoxes():
		for ele in form.CheckBoxes:
			browser.execute_script('document.getElementById("' + ele + '").checked=true')
	def doJS():
		for ele in form.extraJavaScript:
			browser.execute_script(ele)
	def doJSHelp():
		for ele, index in form.extraJSHelper.iteritems():
			browser.execute_script('document.getElementById("' + ele +'").value = "'+ user.getField(index) +'";')
	def submitJS():
		for ele in form.submitJS:
			browser.execute_script(ele)
	doClicks()
	fillField()
	attachField()
	dropDownField()
	dropDownHelper()
	checkBoxes()
	doJS()
	doJSHelp()
	submitJS()
	if not form.submitJS:
		browser.execute_script('document.getElementsByClassName("' + form.finalSubmit + '")[document.getElementsByClassName("' + form.finalSubmit + '").length-1].click()')
	time.sleep(10)
	browser.quit()
	# display.stop()

Affirm = Form("https://jobs.lever.co/affirm/41093734-0492-4f7e-b5ab-7fe53f2143e7/apply", "Affirm")
Affirm.addFillField('name',1, "Full name")
Affirm.addFillField('email',2, "Email")
Affirm.addAttachField('resume',6)
Affirm.addFillField('phone',3, "Phone")
Affirm.addFillField("urls[Github]",12, "Github URL")
Affirm.addFillField("urls[LinkedIn]",13, "LinkedIn URL")
Affirm.addFillField("urls[Other]",14, "Other website")
Affirm.setFinalSubmit('template-btn-submit')

Quora = Form("https://jobs.lever.co/quora/c6456987-4af5-4db0-984e-b8489ffdcf0a/apply", "Quora")
Quora.addFillField('name',1, "Full name")
Quora.addFillField('email',2, "Email")
Quora.addAttachField('resume',6)
Quora.addFillField('phone',3, "Phone")
Quora.addFillField("urls[Github]",12, "Github URL")
Quora.addFillField("urls[LinkedIn]",13, "LinkedIn URL")
Quora.addFillField("urls[Other]",14, "Other website")
Quora.setFinalSubmit('template-btn-submit')

Box = Form("https://jobs.lever.co/box/c0aba64f-7d5d-4e52-b1eb-03460b0f34a6/apply", "Box")
Box.addFillField('name',1, "Full name")
Box.addFillField('email',2, "Email")
Box.addAttachField('resume',6)
Box.addFillField('phone',3, "Phone")
Box.addFillField("urls[Github]",12, "Github URL")
Box.addFillField("urls[LinkedIn]",13, "LinkedIn URL")
Box.addFillField("urls[Other]",14, "Other website")
Box.setFinalSubmit('template-btn-submit')

Stripe = Form("https://stripe.com/jobs/positions/engineer/#engineering", "Stripe")
Stripe.addEmail({"email": "jobs+engineer@stripe.com","name":"Stripe"})

Arista = Form("http://www.arista.com/en/careers/engineering", "Arista")
Arista.addEmail({"email": " jobs@arista.com","name":"Arista"})

EA = Form("http://ea.avature.net/university", "EA")
EA.addAttachField("file_69",6)
EA.addFillField("61",1.1, "First Name")
EA.addFillField("62",1.2, "Last Name / Surname")
EA.addFillField("63",2, "Email")
EA.addFillField("64",3, "Phone")
EA.addFillField("78",4, "University")
EA.addFillField("79",10, "Major")
EA.addDropDownField("67",4)
EA.addDropDownField("145",1)
EA.addCheckBox("80_1")
EA.addCheckBox("128_0")
EA.addCheckBox("74")
EA.setFinalSubmit("saveButton")
EA.addJavaScript('document.getElementById("68").value="2016-05-20"')

Square = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=q8Z9VfwV&j=o2XdZfwV&page=Apply", "Square")
Square.addJSHelper("jvresume",11)
Square.addFillField("jvfirstname",1.1, "First Name")
Square.addFillField("jvlastname",1.2, "Last Name")
Square.addFillField("jvemail",2, "Email")
Square.addFillField("jvphone",3, "Phone")
Square.addFillField("jvfld-xaMmVfwX",4, "College or University Most Recently Attended")
Square.addDropDownField("jvfld-xrNmVfwf",4)
Square.setFinalSubmit("btn")

MongoDB = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?k=Apply&c=qX79VfwS&j=oG2vZfwW", "MongoDB")
MongoDB.addFillField("jvfirstname",1.1, "First Name")
MongoDB.addFillField("jvlastname",1.2, "Last Name")
MongoDB.addFillField("jvemail",2, "Email")
MongoDB.addFillField("jvphone",3, "Phone")
MongoDB.addFillField("jvresume",11, "Resume")
MongoDB.setFinalSubmit("jvbutton")

Nest = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?k=Apply&c=qW69VfwQ&j=oS7wZfwe", "Nest")
Nest.addFillField("jvfirstname",1.1, "First Name")
Nest.addFillField("jvlastname",1.2, "Last Name")
Nest.addFillField("jvemail",2, "Email")
Nest.addFillField("jvphone",3, "Phone")
Nest.addFillField("jvresume",11, "Resume")
Nest.addFillField("jvfld-x-fV9VfwY", 4, "Company")
Nest.addFillField("jvfld-x5jpVfws", 4, "School Name")
Nest.addDropDownField("jvfld-x2jpVfwp", 2)
Nest.addDropDownField("jvfld-x3jpVfwq", 2)
Nest.setFinalSubmit("jvbutton")

SpaceX = Form("https://hire.jobvite.com/CompanyJobs/Careers.aspx?k=Apply&c=qz49Vfwr&j=obTMZfwz&nl=0", "SpaceX")
SpaceX.addFillField("jvfirstname",1.1, "First Name")
SpaceX.addFillField("jvlastname",1.2, "Last Name")
SpaceX.addFillField("jvemail",2, "Email")
SpaceX.addFillField("jvphone",3, "Phone")
SpaceX.addDropDownField("jvfld-xoWgVfwf",1)
SpaceX.addJSHelper("jvresume",11)
SpaceX.setFinalSubmit("jvbutton")

Jawbone = Form("https://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qPb9VfwO&amp;cs=919aVfwZ&amp;j=orRJZfwK&amp;jvprefix=https%3a%2f%2fjawbone.com&amp;jvresize=%2fcareers%2fjobvite_frame_resize&amp;page=Apply&page=Apply&j=orRJZfwK", "Jawbone")
Jawbone.addFillField("jvfirstname",1.1, "First Name")
Jawbone.addFillField("jvlastname",1.2, "Last Name")
Jawbone.addFillField("jvemail",2, "Email")
Jawbone.addFillField("jvphone",3, "Phone")
Jawbone.addJSHelper("jvresume",11)
Jawbone.setFinalSubmit("jvbutton")

RocketFuel = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qK29VfwA&jvprefix=http%3a%2f%2frocketfuel.com&cs=9Sq9Vfw6&jvresize=http%3a%2f%2frocketfuel.com%2fframeresize.htm&page=Apply&j=o7hRZfwY", "RocketFuel")
RocketFuel.addFillField("jvfirstname",1.1,"First Name")
RocketFuel.addFillField("jvlastname",1.2, "Last Name")
RocketFuel.addFillField("jvemail",2, "Email")
RocketFuel.addJavaScript('document.getElementById("Text1").value = "N/A";');
RocketFuel.addFillField("jvfld-x-sV9Vfwb", 8, "City")
RocketFuel.addFillField("jvphone",3, "Phone")
RocketFuel.addDropDownField("jvfld-xFjqVfw3", 2)
RocketFuel.addJSHelper("jvresume",11)
RocketFuel.setFinalSubmit("btnSendApp")
RocketFuel.setSubmitJS("$('#jvform').submit();");

Etsy = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qmZ9Vfw9&amp;j=oMwPZfwQ&amp;page=Apply&page=Apply&j=oMwPZfwQ", "Etsy")
Etsy.addFillField("jvfirstname", 1.1, "First Name")
Etsy.addFillField("jvlastname",1.2, "Last Name")
Etsy.addFillField("jvemail",2, "Email")
Etsy.addFillField("jvphone",3, "Phone")
Etsy.addDropDownField("jvfld-xCBiVfwa", 2)
Etsy.addDropDownField("jvfld-xOKiVfwv", 1)
Etsy.addJSHelper("jvresume",11)
Etsy.setFinalSubmit("jvbutton")

Yelp = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=q6X9VfwR&jvprefix=http%3a%2f%2fwww.yelp.com&cs=924aVfwV&jvresize=http%3a%2f%2fwww.yelp.com%2fhtml%2fjobvite.html&nl=0&page=Apply&j=oFOmWfwv", "Yelp")
Yelp.addFillField("jvfirstname", 1.1, "First Name")
Yelp.addFillField("jvlastname",1.2, "Last Name")
Yelp.addFillField("jvfld-x-sV9Vfwb", 8, "City")
Yelp.addDropDownField("jvfld-x-XV9VfwG", 52)
Yelp.addDropDownField("jvfld-x-uV9Vfwd", 226)
Yelp.addFillField("jvemail",2, "Email")
Yelp.addFillField("jvphone",3, "Phone")
Yelp.addDropDownField("jvworkstatus", 1)
Yelp.addFillField("jvfld-xGGfVfwg", 14, "Portfolio Link")
Yelp.addJSHelper("jvresume",11)
Yelp.setSubmitJS("$('#jvform').submit();");
Yelp.setSubmitJS("document.getElementById('f0')[5].selected=true")
Yelp.setSubmitJS("document.forms[0].submit() ;")

Zendesk = Form("https://hire.jobvite.com/CompanyJobs/Careers.aspx?c=q769Vfw1&jvprefix=http%3a%2f%2fwww.zendesk.com&jvresize=https%3a%2f%2fwww.zendesk.com%2fframe-resize&page=Apply&j=ogCBZfwc", "Zendesk")
Zendesk.addFillField("jvfirstname", 1.1, "First Name")
Zendesk.addFillField("jvlastname",1.2, "Last Name")
Zendesk.addFillField("jvemail",2, "Email")
Zendesk.addFillField("jvphone",3, "Phone")
Zendesk.addJSHelper("jvresume",11)
Zendesk.setFinalSubmit("jvbutton")

AppNexus = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?k=JobListing&c=qbZ9VfwY&jvresize=http%3A%2F%2Fcareers.appnexus.com%2FFrameResize.html&j=oB1QZfwb%2CApply&v=1", "AppNexus")
AppNexus.addFillField("jvfirstname",1.1,"First Name")
AppNexus.addJSHelper("jvresume",11)
AppNexus.addFillField('jvlastname',1.2, "Last Name")
AppNexus.addFillField("jvemail",2, "Email")
AppNexus.addFillField("jvphone",3, "Phone")
AppNexus.addFillField("jvfld-x-sV9Vfwb",4, "University")
AppNexus.addDropDownField("jvfld-x-XV9VfwG",5)
AppNexus.setSubmitJS("$('#jvform').submit();");

Lifesize = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=q9Y9VfwV&page=Apply&j=omdOZfw6", "Lifesize")
Lifesize.addFillField("jvfirstname",1.1, "First Name")
Lifesize.addFillField("jvlastname", 1.2, "Last Name")
Lifesize.addFillField("jvemail", 2, "Email")
Lifesize.addFillField("jvphone",3, "Phone")
Lifesize.addJSHelper("jvresume", 11)
Lifesize.setFinalSubmit("jvbutton")

Medialets = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qCY9Vfwo&jvprefix=http%3a%2f%2fmedialets.com&jvresize=https%3a%2f%2fmedialets.com%2fjv-frame-resize.html&v=1&page=Apply&j=orM8Wfw1", "Medialets")
Medialets.addFillField("jvfirstname", 1.1, "First Name")
Medialets.addFillField("jvlastname", 1.2, "Last Name")
Medialets.addFillField("jvemail", 2, "Email")
Medialets.addFillField("jvphone",3, "Phone")
Medialets.addJSHelper("jvresume", 11)
Medialets.setFinalSubmit("jvbutton")

AppFolio = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qh79Vfwc&jvprefix=http%3a%2f%2fwww.appfolio.com&cs=9QE9Vfwi&jvresize=http%3a%2f%2fwww.appfolio.com%2fjobvite_frame_resize.html&page=Apply&j=osVGZfwM", "AppFolio")
AppFolio.addFillField("jvfirstname", 1.1, "First Name")
AppFolio.addFillField("jvlastname", 1.2, "Last Name")
AppFolio.addFillField("jvemail", 2, "Email")
AppFolio.addFillField("jvphone", 3, "Phone")
AppFolio.addJSHelper("jvresume", 11)
AppFolio.addCheckBox("jvfld-xrtpVfwY")
AppFolio.addFillField("jvfld-xstpVfwZ", 1, "Applicant Initials")
AppFolio.setSubmitJS("$('#jvform').submit();")

Infinera = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qKW9Vfwu&jvprefix=http%3a%2f%2fwww.infinera.com&cs=9eVaVfwY&jvresize=http%3a%2f%2fhttp%3a%2f%2finfinera.boldfocus.com%2fcareer%2fFrameResize.html&page=Apply&j=ooKvZfwm", "Infinera")
Infinera.addFillField("jvfirstname", 1.1, "First Name")
Infinera.addFillField("jvlastname", 1.2, "Last Name")
Infinera.addFillField("jvemail", 2, "Email")
Infinera.addFillField("jvphone", 3, "Phone")
Infinera.addFillField("jvfld-x-sV9Vfwb", 8, "City")
Infinera.addFillField("jvfld-x-XV9VfwG", 9.1, "State")
Infinera.setSubmitJS("$('#jvform').submit();")
Infinera.addJSHelper("jvresume", 11)

InteractiveIntelligence = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qqY9Vfwc&jvprefix=http%3a%2f%2fwww.inin.com&cs=9w4bVfwq&jvresize=http%3a%2f%2fwww.inin.com%2fCareers%2fDocuments%2fframeresize.htm&page=Apply&j=oHUSZfwc", "InteractiveIntelligence")
InteractiveIntelligence.addFillField("jvfirstname", 1.1, "First Name")
InteractiveIntelligence.addFillField("jvlastname", 1.2, "Last Name")
InteractiveIntelligence.addFillField("jvemail", 2, "Email")
InteractiveIntelligence.addFillField("jvphone", 3, "Phone")
InteractiveIntelligence.addDropDownField("jvfld-x-XV9VfwG", 1)
InteractiveIntelligence.addFillField("jvfld-x-sV9Vfwb", 8, "City")
InteractiveIntelligence.addFillField("jvfld-x-tV9Vfwc", 9, "Zipcode")
InteractiveIntelligence.addFillField("jvfld-x-rV9Vfwa", 7, "Address")
InteractiveIntelligence.addJSHelper("jvresume", 11)
InteractiveIntelligence.setSubmitJS("$('#jvform').submit();")

CodeAcademy = Form("https://jobs.lever.co/codecademy/865fcd20-1fcf-47ff-bbfc-67dccdb9322a/apply", "CodeAcademy")
CodeAcademy.addFillField('name',1,"Full Name")
CodeAcademy.addFillField('email',2,"Email")
CodeAcademy.addAttachField('resume',6)
CodeAcademy.addFillField('phone',3,"Phone")
CodeAcademy.addFillField("urls[Github]",12, "Github URL")
CodeAcademy.addFillField("urls[LinkedIn]",13, "LinkedIn URL")
CodeAcademy.addFillField("urls[Other]",14, "Other website")
CodeAcademy.setFinalSubmit('template-btn-submit')
 
ClearSlide = Form("https://jobs.lever.co/clearslide/ba666e4f-221c-4b8e-bb7d-f435d0d1c105/apply", "ClearSlide")
ClearSlide.addFillField('name',1,"Full Name")
ClearSlide.addFillField('email',2,"Email")
ClearSlide.addAttachField('resume', 6)
ClearSlide.addFillField('phone',3,"Phone")
ClearSlide.addFillField("urls[Github]",12, "Github URL")
ClearSlide.addFillField("urls[LinkedIn]",13, "LinkedIn URL")
ClearSlide.addFillField("urls[Other]",14, "Other website")
ClearSlide.setFinalSubmit('template-btn-submit')

Blackbaud = Form("https://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qWX9VfwH&jvprefix=https%3a%2f%2fwww.blackbaud.com&cs=95XaVfwR&jvresize=https%3a%2f%2fwww.blackbaud.com%2ffiles%2fcareers%2fFrameResize.html&nl=0&page=Apply&j=oWGJZfw4", "Blackbaud")
Blackbaud.addFillField("jvfirstname", 1.1, "First Name")
Blackbaud.addFillField("jvlastname", 1.2, "Last Name")
Blackbaud.addFillField("jvemail", 2, "Email")
Blackbaud.addFillField("jvphone", 3, "Phone")
Blackbaud.addFillField("jvfld-x-rV9Vfwa", 7, "Address")
Blackbaud.addFillField("jvfld-x-sV9Vfwb", 8, "City")
Blackbaud.addFillField("jvfld-x-tV9Vfwc", 9, "Zipcode")
Blackbaud.addDropDownField("jvfld-x-uV9Vfwd", 226)
Blackbaud.addDropDownField("jvfld-x-XV9VfwG", 1)
Blackbaud.addJSHelper("jvresume", 11)
Blackbaud.setSubmitJS("$('#jvform').submit();")
Blackbaud.setSubmitJS('document.getElementById("f0").value="moo";')
Blackbaud.setSubmitJS('document.getElementById("f2_1").checked=true;')
Blackbaud.setSubmitJS('document.getElementById("f1").value="$1500-$4500";')
Blackbaud.setSubmitJS('document.forms[0].submit();')

SurveyMonkey = Form("https://boards.greenhouse.io/surveymonkey/jobs/30035?#app", "SurveyMonkey")
SurveyMonkey.addFillField('job_application[first_name]',1.1, "First name")
SurveyMonkey.addFillField('job_application[last_name]',1.2, "Last name")
SurveyMonkey.addFillField('job_application[email]',2, "Email")
SurveyMonkey.addFillField('job_application[phone]',3, "Phone")
SurveyMonkey.addFillField('job_application[answers_attributes][0][text_value]',13, "Linkedin")
SurveyMonkey.addFillField('job_application[answers_attributes][1][text_value]',14, "Personal Website")
SurveyMonkey.hasGreenHouseResume()
SurveyMonkey.setFinalSubmit("button")

ThumbTack = Form("https://boards.greenhouse.io/thumbtack/jobs/2570?#app", "ThumbTack")
ThumbTack.addFillField('job_application[first_name]',1.1, "First name")
ThumbTack.addFillField('job_application[last_name]',1.2, "Last name")
ThumbTack.addFillField('job_application[email]',2, "Email")
ThumbTack.addFillField('job_application[phone]',3, "Phone")
ThumbTack.addFillField('job_application[answers_attributes][0][text_value]',13, "Linkedin")
ThumbTack.addFillField('job_application[answers_attributes][1][text_value]',14, "Personal website")
ThumbTack.hasGreenHouseResume()
ThumbTack.setFinalSubmit("button")

Twilio = Form("https://boards.greenhouse.io/twilio/jobs/26688#app", "Twilio")
Twilio.addFillField('job_application[first_name]',1.1, "First name")
Twilio.addFillField('job_application[last_name]',1.2, "Last name")
Twilio.addFillField('job_application[email]',2, "Email")
Twilio.addFillField('job_application[phone]',3, "Phone")
Twilio.addJavaScript('document.getElementById("job_application_answers_attributes_0_text_value").value = "Napkins.io"')
Twilio.addFillField('job_application[answers_attributes][2][text_value]',13, "Linkedin")
Twilio.addFillField('job_application[answers_attributes][3][text_value]',14, "Personal website")
Twilio.hasGreenHouseResume()
Twilio.setFinalSubmit("button")

TubeMogul = Form("https://boards.greenhouse.io/tubemogulinc/jobs/33121?#app", "TubeMogul")
TubeMogul.addFillField('job_application[first_name]',1.1, "First name")
TubeMogul.addFillField('job_application[last_name]',1.2, "Last name")
TubeMogul.addFillField('job_application[email]',2, "Email")
TubeMogul.addFillField('job_application[phone]',3, "Phone")
TubeMogul.addJavaScript('document.getElementById("job_application_answers_attributes_2_text_value").value = "Napkins.io"')
TubeMogul.addDropDownField("job_application_answers_attributes_3_boolean_value", 2)
TubeMogul.hasGreenHouseResume()
TubeMogul.setFinalSubmit("button")

Pinterest = Form("https://app.greenhouse.io/embed/job_app?token=34498&amp;t=null&amp;b=https://about.pinterest.com/en/careers/cloud-software-engineer-intern_34498", "Pinterest")
Pinterest.addFillField('job_application[first_name]',1.1, "First name")
Pinterest.addFillField('job_application[last_name]',1.2, "Last name")
Pinterest.addFillField('job_application[email]',2, "Email")
Pinterest.addFillField('job_application[phone]',3, "Phone")
Pinterest.hasGreenHouseResume()
Pinterest.addJavaScript('document.getElementById("job_application_answers_attributes_0_text_value").value = "N/A"')
Pinterest.addFillField("job_application[answers_attributes][1][text_value]",13, "Linkedin")
Pinterest.addFillField("job_application[answers_attributes][2][text_value]",12, "Github")
Pinterest.addFillField("job_application[answers_attributes][3][text_value]",14, "Personal")
Pinterest.setFinalSubmit("button")

Spokeo = Form("https://boards.greenhouse.io/spokeo/jobs/33554#app", "Spokeo")
Spokeo.addFillField('job_application[first_name]',1.1, "First name")
Spokeo.addFillField('job_application[last_name]',1.2, "Last name")
Spokeo.addFillField('job_application[email]',2, "Email")
Spokeo.addFillField('job_application[phone]',3, "Phone")
Spokeo.hasGreenHouseResume()
Spokeo.addFillField("job_application[answers_attributes][0][text_value]",13, "Linkedin")
Spokeo.addFillField("job_application[answers_attributes][1][text_value]",14, "Personal website")
Spokeo.setFinalSubmit("button")

form_dict = {'Quora':Quora, 'Box':Box, 'Affirm':Affirm, 'Stripe':Stripe, 'Arista':Arista, 'EA':EA, 'Square':Square, 'MongoDB':MongoDB, 'Nest':Nest, 'SpaceX':SpaceX, 'Jawbone':Jawbone, 'Etsy':Etsy, 'Yelp':Yelp, 'Zendesk':Zendesk, 'AppNexus':AppNexus, 'RocketFuel':RocketFuel, 'Lifesize':Lifesize, 'Medialets':Medialets, "AppFolio":AppFolio, 'Infinera':Infinera, "InteractiveIntelligence":InteractiveIntelligence, 'Spokeo':Spokeo, 'Pinterest':Pinterest, 'TubeMogul':TubeMogul, 'Twilio':Twilio, 'ThumbTack':ThumbTack, 'SurveyMonkey':SurveyMonkey, 'Blackbaud':Blackbaud, 'CodeAcademy':CodeAcademy, 'ClearSlide':ClearSlide}