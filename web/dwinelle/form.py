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
	def addEmail(self,em):
		self.email = em
	def addClicks(self, button_name):
		self.html_button_clicks.append(button_name)
	def addFillField(self, html_ele, field_num):
		self.Fill_Fields[html_ele] = field_num
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

def form_fill(user, form):
	display = Display(visible=0, size=(800, 600))
	display.start()
	if form.email != {}:
		st = "Hello " + form.email["name"] +",\nMy name is " + user.getField(1)  +  " and I am currently a student at " + user.getField(4) + ". I am applying for the Software Engineering Internship position for summer 2015. I can be reached at " + user.getField(2) + " or " + user.getField(3)+ ".\
		\nBest,\n" + user.getField(1)
		email_send("Software Internship Application",st,[form.email['email'], user.getField(2)],attachment=user.getField(6))
		return
	browser = Browser()
	browser.visit(form.url)
	def doClicks(): #partial_htmls being dealt with
		for ele in form.html_button_clicks:
			browser.find_link_by_partial_href(ele)[0].click()
	def fillField():
		for ele, field in form.Fill_Fields.iteritems():
			browser.fill(ele,user.getField(field))
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
	display.stop()

Counsyl = Form("https://www.counsyl.com/careers/software-engineering-intern-2015/", "Counsyl")
Counsyl.addClicks("https://jobs.lever.co/counsyl/")
Counsyl.addFillField('name',1)
Counsyl.addFillField('email',2)
Counsyl.addFillField('phone',3)
Counsyl.addFillField('cards[966e5478-a369-466c-bcb5-82e09e928bcc][field0]',4)
Counsyl.addFillField('cards[966e5478-a369-466c-bcb5-82e09e928bcc][field1]',5)
Counsyl.addDropDownField('$m',1)
Counsyl.addAttachField('resume',6)
Counsyl.addFillField("urls[Github]",12)
Counsyl.addFillField("urls[LinkedIn]",13)
Counsyl.addFillField("urls[Other]",14)
Counsyl.addAttachField('cards[86665ab6-19bd-4fd0-a466-96f3acc9ccb9][field0]',6)
Counsyl.setFinalSubmit('template-btn-submit')

Affirm = Form("https://jobs.lever.co/affirm/41093734-0492-4f7e-b5ab-7fe53f2143e7/apply", "Affirm")
Affirm.addFillField('name',1)
Affirm.addFillField('email',2)
Affirm.addAttachField('resume',6)
Affirm.addFillField('phone',3)
Affirm.addFillField("urls[Github]",12)
Affirm.addFillField("urls[LinkedIn]",13)
Affirm.addFillField("urls[Other]",14)
Affirm.setFinalSubmit('template-btn-submit')

Quora = Form("https://jobs.lever.co/quora/c6456987-4af5-4db0-984e-b8489ffdcf0a/apply", "Quora")
Quora.addFillField('name',1)
Quora.addFillField('email',2)
Quora.addAttachField('resume',6)
Quora.addFillField('phone',3)
Quora.addFillField("urls[Github]",12)
Quora.addFillField("urls[LinkedIn]",13)
Quora.addFillField("urls[Other]",14)
Quora.setFinalSubmit('template-btn-submit')

Box = Form("https://jobs.lever.co/box/c0aba64f-7d5d-4e52-b1eb-03460b0f34a6/apply", "Box")
Box.addFillField('name',1)
Box.addFillField('email',2)
Box.addAttachField('resume',6)
Box.addFillField('phone',3)
Box.addFillField("urls[Github]",12)
Box.addFillField("urls[LinkedIn]",13)
Box.addFillField("urls[Other]",14)
Box.setFinalSubmit('template-btn-submit')

Stripe = Form("https://stripe.com/jobs/positions/engineer/#engineering", "Stripe")
Stripe.addEmail({"email": "jobs+engineer@stripe.com","name":"Stripe"})

Arista = Form("http://www.arista.com/en/careers/engineering", "Arista")
Arista.addEmail({"email": " jobs@arista.com","name":"Arista"})

EA = Form("http://ea.avature.net/university", "EA")
EA.addAttachField("file_69",6)
EA.addFillField("61",1.1)
EA.addFillField("62",1.2)
EA.addFillField("63",2)
EA.addFillField("64",3)
EA.addFillField("78",4)
EA.addFillField("79",10)
EA.addDropDownField("67",4)
EA.addDropDownField("145",1)
EA.addCheckBox("80_1")
EA.addCheckBox("128_0")
EA.addCheckBox("74")
EA.setFinalSubmit("saveButton")
EA.addJavaScript('document.getElementById("68").value="2016-05-20"')

Square = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=q8Z9VfwV&j=o2XdZfwV&page=Apply", "Square")
Square.addJSHelper("jvresume",11)
Square.addFillField("jvfirstname",1.1)
Square.addFillField("jvlastname",1.2)
Square.addFillField("jvemail",2)
Square.addFillField("jvphone",3)
Square.addFillField("jvfld-xaMmVfwX",4)
Square.addDropDownField("jvfld-xrNmVfwf",4)
Square.setFinalSubmit("btn")

MongoDB = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?k=Apply&c=qX79VfwS&j=oG2vZfwW", "MongoDB")
MongoDB.addFillField("jvfirstname",1.1)
MongoDB.addFillField("jvlastname",1.2)
MongoDB.addFillField("jvemail",2)
MongoDB.addFillField("jvphone",3)
MongoDB.addFillField("jvresume",11)
MongoDB.setFinalSubmit("jvbutton")

Nest = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?k=Apply&c=qW69VfwQ&j=oS7wZfwe", "Nest")
Nest.addFillField("jvfirstname",1.1)
Nest.addFillField("jvlastname",1.2)
Nest.addFillField("jvemail",2)
Nest.addFillField("jvphone",3)
Nest.addFillField("jvresume",11)
Nest.addFillField("jvfld-x-fV9VfwY", 4)
Nest.addFillField("jvfld-x5jpVfws", 4)
Nest.addDropDownField("jvfld-x2jpVfwp", 2)
Nest.addDropDownField("jvfld-x3jpVfwq", 2)
Nest.setFinalSubmit("jvbutton")

SpaceX = Form("https://hire.jobvite.com/CompanyJobs/Careers.aspx?k=Apply&c=qz49Vfwr&j=obTMZfwz&nl=0", "SpaceX")
SpaceX.addFillField("jvfirstname",1.1)
SpaceX.addFillField("jvlastname",1.2)
SpaceX.addFillField("jvemail",2)
SpaceX.addFillField("jvphone",3)
SpaceX.addDropDownField("jvfld-xoWgVfwf",1)
SpaceX.addJSHelper("jvresume",11)
SpaceX.setFinalSubmit("jvbutton")

Jawbone = Form("https://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qPb9VfwO&amp;cs=919aVfwZ&amp;j=orRJZfwK&amp;jvprefix=https%3a%2f%2fjawbone.com&amp;jvresize=%2fcareers%2fjobvite_frame_resize&amp;page=Apply&page=Apply&j=orRJZfwK", "Jawbone")
Jawbone.addFillField("jvfirstname",1.1)
Jawbone.addFillField("jvlastname",1.2)
Jawbone.addFillField("jvemail",2)
Jawbone.addFillField("jvphone",3)
Jawbone.addJSHelper("jvresume",11)
Jawbone.setFinalSubmit("jvbutton")

RocketFuel = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qK29VfwA&jvprefix=http%3a%2f%2frocketfuel.com&cs=9Sq9Vfw6&jvresize=http%3a%2f%2frocketfuel.com%2fframeresize.htm&page=Apply&j=o7hRZfwY", "RocketFuel")
RocketFuel.addFillField("jvfirstname",1.1)
RocketFuel.addFillField("jvlastname",1.2)
RocketFuel.addFillField("jvemail",2)
RocketFuel.addJavaScript('document.getElementById("Text1").value = "N/A";');
RocketFuel.addFillField("jvfld-x-sV9Vfwb", 8)
RocketFuel.addFillField("jvphone",3)
RocketFuel.addDropDownField("jvfld-xFjqVfw3", 2)
RocketFuel.addJSHelper("jvresume",11)
RocketFuel.setFinalSubmit("btnSendApp")
RocketFuel.setSubmitJS("$('#jvform').submit();");

Etsy = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qmZ9Vfw9&amp;j=oMwPZfwQ&amp;page=Apply&page=Apply&j=oMwPZfwQ", "Etsy")
Etsy.addFillField("jvfirstname", 1.1)
Etsy.addFillField("jvlastname",1.2)
Etsy.addFillField("jvemail",2)
Etsy.addFillField("jvphone",3)
Etsy.addDropDownField("jvfld-xCBiVfwa", 2)
Etsy.addDropDownField("jvfld-xOKiVfwv", 1)
Etsy.addJSHelper("jvresume",11)
Etsy.setFinalSubmit("jvbutton")

Yelp = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=q6X9VfwR&jvprefix=http%3a%2f%2fwww.yelp.com&cs=924aVfwV&jvresize=http%3a%2f%2fwww.yelp.com%2fhtml%2fjobvite.html&nl=0&page=Apply&j=oFOmWfwv", "Yelp")
Yelp.addFillField("jvfirstname", 1.1)
Yelp.addFillField("jvlastname",1.2)
Yelp.addFillField("jvfld-x-sV9Vfwb", 8)
Yelp.addDropDownField("jvfld-x-XV9VfwG", 52)
Yelp.addDropDownField("jvfld-x-uV9Vfwd", 226)
Yelp.addFillField("jvemail",2)
Yelp.addFillField("jvphone",3)
Yelp.addDropDownField("jvworkstatus", 1)
Yelp.addFillField("jvfld-xGGfVfwg", 14)
Yelp.addJSHelper("jvresume",11)
Yelp.setSubmitJS("$('#jvform').submit();");
Yelp.setSubmitJS("document.getElementById('f0')[5].selected=true")
Yelp.setSubmitJS("document.forms[0].submit() ;")

Zendesk = Form("https://hire.jobvite.com/CompanyJobs/Careers.aspx?c=q769Vfw1&jvprefix=http%3a%2f%2fwww.zendesk.com&jvresize=https%3a%2f%2fwww.zendesk.com%2fframe-resize&page=Apply&j=ogCBZfwc", "Zendesk")
Zendesk.addFillField("jvfirstname", 1.1)
Zendesk.addFillField("jvlastname",1.2)
Zendesk.addFillField("jvemail",2)
Zendesk.addFillField("jvphone",3)
Zendesk.addJSHelper("jvresume",11)
Zendesk.setFinalSubmit("jvbutton")

AppNexus = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?k=JobListing&c=qbZ9VfwY&jvresize=http%3A%2F%2Fcareers.appnexus.com%2FFrameResize.html&j=oB1QZfwb%2CApply&v=1", "AppNexus")
AppNexus.addFillField("jvfirstname",1.1)
AppNexus.addJSHelper("jvresume",11)
AppNexus.addJSHelper('jvlastname',1.2)
AppNexus.addJSHelper("jvemail",2)
AppNexus.addJSHelper("jvphone",3)
AppNexus.addJSHelper("jvresume",11)
AppNexus.addFillField("jvfld-x-sV9Vfwb",4)
AppNexus.addDropDownField("jvfld-x-XV9VfwG",5)
AppNexus.setSubmitJS("$('#jvform').submit();");

Lifesize = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=q9Y9VfwV&page=Apply&j=omdOZfw6", "Lifesize")
Lifesize.addFillField("jvfirstname",1.1)
Lifesize.addFillField("jvlastname", 1.2)
Lifesize.addFillField("jvemail", 2)
Lifesize.addFillField("jvphone",3)
Lifesize.addJSHelper("jvresume", 11)
Lifesize.setFinalSubmit("jvbutton")

Medialets = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qCY9Vfwo&jvprefix=http%3a%2f%2fmedialets.com&jvresize=https%3a%2f%2fmedialets.com%2fjv-frame-resize.html&v=1&page=Apply&j=orM8Wfw1", "Medialets")
Medialets.addFillField("jvfirstname", 1.1)
Medialets.addFillField("jvlastname", 1.2)
Medialets.addFillField("jvemail", 2)
Medialets.addFillField("jvphone",3)
Medialets.addJSHelper("jvresume", 11)
Medialets.setFinalSubmit("jvbutton")

AppFolio = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qh79Vfwc&jvprefix=http%3a%2f%2fwww.appfolio.com&cs=9QE9Vfwi&jvresize=http%3a%2f%2fwww.appfolio.com%2fjobvite_frame_resize.html&page=Apply&j=osVGZfwM", "AppFolio")
AppFolio.addFillField("jvfirstname", 1.1)
AppFolio.addFillField("jvlastname", 1.2)
AppFolio.addFillField("jvemail", 2)
AppFolio.addFillField("jvphone", 3)
AppFolio.addJSHelper("jvresume", 11)
AppFolio.addCheckBox("jvfld-xrtpVfwY")
AppFolio.addFillField("jvfld-xstpVfwZ", 1)
AppFolio.setSubmitJS("$('#jvform').submit();")

Infinera = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qKW9Vfwu&jvprefix=http%3a%2f%2fwww.infinera.com&cs=9eVaVfwY&jvresize=http%3a%2f%2fhttp%3a%2f%2finfinera.boldfocus.com%2fcareer%2fFrameResize.html&page=Apply&j=ooKvZfwm", "Infinera")
Infinera.addFillField("jvfirstname", 1.1)
Infinera.addFillField("jvlastname", 1.2)
Infinera.addFillField("jvemail", 2)
Infinera.addFillField("jvphone", 3)
Infinera.addFillField("jvfld-x-sV9Vfwb", 8)
Infinera.addFillField("jvfld-x-XV9VfwG", 9.1)
Infinera.setSubmitJS("$('#jvform').submit();")
Infinera.addJSHelper("jvresume", 11)

InteractiveIntelligence = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qqY9Vfwc&jvprefix=http%3a%2f%2fwww.inin.com&cs=9w4bVfwq&jvresize=http%3a%2f%2fwww.inin.com%2fCareers%2fDocuments%2fframeresize.htm&page=Apply&j=oHUSZfwc", "InteractiveIntelligence")
InteractiveIntelligence.addFillField("jvfirstname", 1.1)
InteractiveIntelligence.addFillField("jvlastname", 1.2)
InteractiveIntelligence.addFillField("jvemail", 2)
InteractiveIntelligence.addFillField("jvphone", 3)
InteractiveIntelligence.addDropDownField("jvfld-x-XV9VfwG", 1)
InteractiveIntelligence.addFillField("jvfld-x-sV9Vfwb", 8)
InteractiveIntelligence.addFillField("jvfld-x-tV9Vfwc", 9)
InteractiveIntelligence.addFillField("jvfld-x-rV9Vfwa", 7)
InteractiveIntelligence.addJSHelper("jvresume", 11)
InteractiveIntelligence.setSubmitJS("$('#jvform').submit();")

form_dict = {'Quora':Quora, 'Box':Box, 'Counsyl':Counsyl, 'Affirm':Affirm, 'Stripe':Stripe, 'Arista':Arista, 'EA':EA, 'Square':Square, 'MongoDB':MongoDB, 'Nest':Nest, 'SpaceX':SpaceX, 'Jawbone':Jawbone, 'Etsy':Etsy, 'Yelp':Yelp, 'Zendesk':Zendesk, 'AppNexus':AppNexus, 'RocketFuel':RocketFuel, 'Lifesize':Lifesize, 'Medialets':Medialets, "AppFolio":AppFolio, 'Infinera':Infinera, "InteractiveIntelligence":InteractiveIntelligence}
