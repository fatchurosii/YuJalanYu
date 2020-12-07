import midtransclient

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, CreateView
from django.urls import reverse, reverse_lazy
from .models import modelTransaksi
from django.contrib.auth.models import User
from Paket.models import modelPaket
from .form import TransaksiForm


# Create your views here.
class checkOut(CreateView):
	model = modelTransaksi
	form_class = TransaksiForm
	template_name = 'transaksi/checkOut.html'

	# context_object_name = 'paket_object'

	def get_context_data(self, **kwargs):
		data = modelPaket.objects.get(slug=self.kwargs['slug'])
		extra_context = {
			'title': 'CheckOut',
			'data': data
		}
		self.kwargs.update(extra_context)
		kwargs = self.kwargs
		return super().get_context_data(**kwargs)

	def post(self, request, **kwargs):
		paket = modelPaket.objects.get(slug=request.POST['Paket'])
		user = User.objects.get(email=request.POST['User'])
		snap = midtransclient.Snap(
			is_production=False,
			server_key='SB-Mid-server-uoBpcWvYMzSk72FbVUEUcPox',
			client_key='SB-Mid-client-EOjbQuFJwheGValW')

		jumlah = int(request.POST['jumlah'])
		param = {
			"transaction_details": {
				"order_id": f"order-{request.POST['csrfmiddlewaretoken'][0:5]}",
				"gross_amount": (jumlah * paket.harga),
				"customer_email": user.email
			},
			"credit_card": {
				"secure": True
			}}
		print(param)
		token = snap.create_transaction_token(param)
		print("request : ", request.POST)
		print("token : ", token)

		# save = self.form_class({'paket': paket, 'user': user, 'jumlah': })
		return HttpResponseRedirect(reverse('paket:view'))
