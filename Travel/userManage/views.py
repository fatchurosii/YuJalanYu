from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .models import modelUser
from .form import formUser

# Create your views here.
class Login(LoginView):
<<<<<<< HEAD
	model = modelUser
	form_class = formUser
=======
	# model = modelUser
	# form_class = formUser
>>>>>>> 48f5e775fc74386d1e1acec6731ca75c371c3745
	template_name = 'User/login.html'
	success_url = reverse_lazy('home')

	extra_context = {
		'title':'LOGIN'
	}
	query_string = True

	def get(self, request, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('home')
		return self.render_to_response(self.get_context_data())

	def get_context_data(self, **kwargs):
	    self.kwargs.update(self.extra_context)
	    kwargs = self.kwargs
	    return super().get_context_data()

	def get_success_url(self):
		url = self.request.GET.get('next', False)
		if url is False:
			return self.success_url
		else:
			self.success_url = self.request.GET['next']
			return self.success_url

class Logout(LogoutView):
	next_page = reverse_lazy('home')





