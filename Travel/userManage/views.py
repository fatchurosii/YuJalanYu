from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
class Login(LoginView):
	template_name = 'User/login.html'
	success_url = reverse_lazy('home')

	extra_context = {
		'title':'LOGIN'
	}

	def get_context_data(self, **kwargs):
	    self.kwargs.update(self.extra_context)
	    kwargs = self.kwargs
	    return super().get_context_data()

	def get_success_url(self):
		return self.success_url

# class Logout(Logout):
# 	pass