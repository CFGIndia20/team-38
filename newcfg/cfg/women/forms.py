from django import forms
from .models import *

class WomenForm(forms.ModelForm):
	class Meta:
		model= Women
		fields= "__all__"

class ProgressionForm(forms.ModelForm):
    class Meta:
        model = Progression
        fields = "__all__"