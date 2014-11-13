from django import template
register = template.Library()

@register.filter(name='is_resume')
def is_resume(field):
	return field.label == "resume"
