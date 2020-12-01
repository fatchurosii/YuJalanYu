from django import forms
from .models import modelUser


class formUser(forms.ModelForm):

	class Meta:
		model = modelUser
		fields = '__all__'
	
