from django import forms
from django.forms import ModelForm 
from django.utils import timezone
from adminapp.models import Session,Task


class SessionForm(ModelForm):

	session_date=forms.DateTimeField(initial=timezone.now)
	class Meta:
		model = Session
		fields = '__all__'

class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = '__all__'
