from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class formUser(UserCreationForm):
	password1 = forms.CharField(
		label= "Password",
		strip=False,
		widget= forms.PasswordInput(attrs={
			'class':'form-control',
			'placeholder':"Password"
			}),
		)

	password2 = forms.CharField(
		label= "Confirm Password",
		strip=False,
		widget= forms.PasswordInput(attrs={
			'class':'form-control',
			'placeholder':"Confirm Password"
			}),
		)

	class Meta:
		model = User
		fields = ["username", "email", 'password1']
		widgets = {
			'username': forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':"Username"
				}),
			'email': forms.EmailInput(attrs={
				'class':'form-control',
				'placeholder':"Email address"
				})
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['password1']
		self.fields['password2']


	# def clean_password2(self):
	# 	print("Ini Password 1")
	# 	password1 = self.cleaned_data.get("password1")
	# 	password2 = self.cleaned_data.get("password2")
	# 	print(password1)
	# 	if password1 is password2:
	# 		print(True)
	# 		return password2
	# 	else:
	# 		print(False)
	# 		raise forms.ValidationError("Password Tidak Sesuai")

	# def clean(self):
	# 	print("Ini Password 2")
	# 	password1 = self.cleaned_data.get("password1")
	# 	password2 = self.cleaned_data.get("password2")
		
	# 	if password1 is password2:
	# 		print(True)
	# 		return password1
	# 	else:
	# 		print(False)
	# 		raise forms.ValidationError("Password Salah : ")

	
