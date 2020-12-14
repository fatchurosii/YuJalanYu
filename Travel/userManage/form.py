from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class formUser(UserCreationForm):
	class Meta:
		model = User
		fields = ["username", "email"]

	def clean_password2(self):
		print("Ini Password 1")
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		print(password1)
		if password1 is password2:
			print(True)
			return password2
		else:
			print(False)
			raise forms.ValidationError("Password Salah : ")

	# def clean_password2(self):
	# 	print("Ini Password 2")
	# 	password1 = self.cleaned_data.get("password1")
	# 	password2 = self.cleaned_data.get("password2")
		
	# 	if password1 is password2:
	# 		print(True)
	# 		return password1
	# 	else:
	# 		print(False)
	# 		raise forms.ValidationError("Password Salah : ")

	
