from dwinelle.form import *
from dwinelle.user import *

def preview(user, form=Square):
	preview_dict = {}

	if form.email:
		preview_dict['email'] = emailFill(user,form)
		return preview_dict

	for html, tple in form.Fill_Fields.iteritems():
		field, name = tple
		preview_dict[name] = user.getField(field)

	return preview_dict
