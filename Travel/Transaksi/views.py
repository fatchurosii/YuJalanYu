import midtransclient

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, CreateView, ListView
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

		data = self.form_class({'paket': paket, 'user': user, 'jumlah': jumlah,
								'totalHarga': (jumlah * paket.harga), 'token': token, 'status': 'pendding'})
		data.save()
		print(data)
		return HttpResponseRedirect(reverse('transaksi:final', token=data.token))

class DetailCheckOut(DetailView):
	model = modelTransaksi
	context_object_name = "object"
	template_name = 'transaksi/checkOut_Final.html'
	extra_context = {
		'title': "CHECKOUT FINAL"
	}
	pk_url_kwarg = 'token'
	query_string = True

	def get_queryset(self):
		url = self.request.GET.get('token', False)
		if not url:
			print(url)
			self.queryset = self.model.objects.get(token=url)
			return self.queryset
		else:
			self.queryset = None
			return self.queryset

	def get(self, *args, **kwargs):
		if self.query_string:
			if self.request.GET.get('token', False) is False:
				return HttpResponseRedirect(reverse('paket:view'))
		return super().get(self.request, *args, **kwargs)
