import midtransclient

from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from .models import modelTransaksi
from Paket.models import modelPaket

# Create your views here.
class checkOut(DetailView):
	model = modelPaket
	template_name = 'transaksi/checkOut.html'
	extra_context = {
		'title':'CheckOut',
		'data': "data"
		}
	context_object_name = 'paket_object'

	def post(self):
		snap = midtransclient.Snap(
			    is_production=False,
			    server_key='YOUR_SERVER_KEY',
			    client_key='YOUR_CLIENT_KEY'
				)

		