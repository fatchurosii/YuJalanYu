from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormMixin
from django.views.generic import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .form import formUser

# Create your views here.
class Login(LoginView):
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

class createUser(CreateView):
	model = User
	form_class = formUser
	template_name='User/createUser.html'
	extra_context = {
		'title':'Register User',
	}
	success_url = reverse_lazy('home')

	def post(self, request):
		form = self.get_form()
		print("Form : ", form.data)
		print(self.request.POST)
		print("password 1 : ", self.request.POST.get('password1', False))
		print("Password 2 : ", self.request.POST.get('password2', False))
		if form.is_valid():
			print(form.is_valid())
			return redirect('home')
		else:
			print(form.is_valid())
			return super().post(request)
		

# class createUser(FormView):
# 	form_class = formUser
# 	template_name = 'User/createUser.html'
# 	success_url = reverse_lazy('home')

# 	def form_valid(self, form):
# 		form.save()
# 		return super(createUser, self).form_valid(form)

# 	def post(self, request):
# 		form = self.get_form()
# 		if form.is_valid():
# 			print(True)
# 			print(form.is_valid())
# 		else:
# 			print(False)
# 			print(form)
# 		return redirect('home')




