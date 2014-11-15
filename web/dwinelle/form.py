from splinter.browser import Browser
from pyvirtualdisplay import Display 
import time
import os
from soda.email import email_send

class Form:
	def __init__(self,url):
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
	def checkBoxes():          #CHANGEDDDDDDDDDD
		for ele in form.CheckBoxes:
			browser.execute_script('document.getElementById("' + ele + '").checked=true')
	def doJS():
		for ele in form.extraJavaScript:
			browser.execute_script(ele)
	def doJSHelp():
		for ele, index in form.extraJSHelper.iteritems():
			browser.execute_script('document.getElementById("' + ele +'").value = "'+ user.getField(index) +'";')
	doClicks()
	fillField()
	attachField()
	dropDownField()
	dropDownHelper()
	checkBoxes()
	doJS()
	doJSHelp()
	browser.execute_script('document.getElementsByClassName("' + form.finalSubmit + '")[document.getElementsByClassName("' + form.finalSubmit + '").length-1].click()')
	time.sleep(10)
	browser.quit()
	display.stop()

Counsyl = Form("https://www.counsyl.com/careers/software-engineering-intern-2015/")
Counsyl.addClicks("https://jobs.lever.co/counsyl/")
Counsyl.addFillField('name',1)
Counsyl.addFillField('email',2)
Counsyl.addFillField('phone',3)
Counsyl.addFillField('cards[966e5478-a369-466c-bcb5-82e09e928bcc][field0]',4) #Implement findByID Instead
Counsyl.addFillField('cards[966e5478-a369-466c-bcb5-82e09e928bcc][field1]',5) #Implement findByID Instead
Counsyl.addDropDownField('$m',1)
Counsyl.addAttachField('resume',6)
Counsyl.addAttachField('cards[86665ab6-19bd-4fd0-a466-96f3acc9ccb9][field0]',6)
Counsyl.setFinalSubmit('template-btn-submit')

Affirm = Form("https://jobs.lever.co/affirm/41093734-0492-4f7e-b5ab-7fe53f2143e7/apply")
Affirm.addFillField('name',1)
Affirm.addFillField('email',2)
Affirm.addAttachField('resume',6)
Affirm.addFillField('phone',3)
Affirm.setFinalSubmit('template-btn-submit')

Quora = Form("https://jobs.lever.co/quora/c6456987-4af5-4db0-984e-b8489ffdcf0a/apply")
Quora.addFillField('name',1)
Quora.addFillField('email',2)
Quora.addAttachField('resume',6)
Quora.addFillField('phone',3)
Quora.setFinalSubmit('template-btn-submit')

Box = Form("https://jobs.lever.co/box/c0aba64f-7d5d-4e52-b1eb-03460b0f34a6/apply")
Box.addFillField('name',1)
Box.addFillField('email',2)
Box.addAttachField('resume',6)
Box.addFillField('phone',3)
Box.setFinalSubmit('template-btn-submit')

Stripe = Form("https://stripe.com/jobs/positions/engineer/#engineering")
Stripe.addEmail({"email": "jobs+engineer@stripe.com","name":"Stripe"})

Arista = Form("http://www.arista.com/en/careers/engineering")
Arista.addEmail({"email": " jobs@arista.com","name":"Arista"})

EA = Form("http://ea.avature.net/university")
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

Square = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=q8Z9VfwV&j=o2XdZfwV&page=Apply")
Square.addJSHelper("jvresume",11)
Square.addFillField("jvfirstname",1.1)
Square.addFillField("jvlastname",1.2)
Square.addFillField("jvemail",2)
Square.addFillField("jvphone",3)
Square.addFillField("jvfld-xaMmVfwX",4)
Square.addDropDownField("jvfld-xrNmVfwf",4)
Square.setFinalSubmit("btn")

MongoDB = Form("http://hire.jobvite.com/CompanyJobs/Careers.aspx?k=Apply&c=qX79VfwS&j=oG2vZfwW")
MongoDB.addFillField("jvfirstname",1.1)
MongoDB.addFillField("jvlastname",1.2)
MongoDB.addFillField("jvemail",2)
MongoDB.addFillField("jvphone",3)
MongoDB.addFillField("jvresume",11)
MongoDB.setFinalSubmit("jvbutton")

form_dict = {'Quora':Quora, 'Box':Box, 'Counsyl':Counsyl, 'Affirm':Affirm, 'Stripe':Stripe, 'Arista':Arista, 'EA':EA, 'Square':Square, 'MongoDB':MongoDB}
