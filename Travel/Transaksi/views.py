import midtransclient

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, CreateView, ListView
from django.urls import reverse, reverse_lazy
from .models import modelTransaksi
from django.contrib.auth.models import User
from Paket.models import modelPaket
from .form import TransaksiForm
from django.views.decorators.csrf import csrf_protect


# Create your views here.

class checkOut(CreateView):
	model = modelTransaksi
	form_class = TransaksiForm
	# template_name = 'transaksi/checkOut.html'
	query_string = True

	def get(self, request):
		return HttpResponseRedirect(reverse('paket:view'))

	def post(self, request):
		paket = modelPaket.objects.get(slug=request.POST['paket'])
		user = User.objects.get(email=request.POST['user'])
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
			"enabled_payments": [ "bca_klikbca", "bca_klikpay", "bca_va", "bni_va", "gopay", "indomaret"],
			"credit_card": {
				"secure": False,
				"bca_va": {
	        	"free_text": {
	            "inquiry": [
	                {
	                    "id": "text in Bahasa Indonesia"
	                }
	            ],
	            "payment": [
	                {
	                    "id": "text in Bahasa Indonesia"
	                }
	            ]
	        }
},
			}}
		print(param)
		token = snap.create_transaction(param)
		print("request : ", request.POST)
		print("token : ", token)

		data = self.form_class({'paket': paket, 'user': user, 'jumlah': jumlah,
								'totalHarga': (jumlah * paket.harga), 'token': token['token'], 'status': 'pendding'})
		data.save()
		print(data['token'].data)
		return HttpResponseRedirect("%s?token={}".format(data['token'].data) % (reverse('transaksi:final')))
		
class DetailCheckOut(DetailView):
	model = modelTransaksi
	context_object_name = "object"
	template_name = 'transaksi/checkOut_Final.html'
	pk_url_kwarg = 'token'
	query_string = True

	def get_context_data(self, *args,**kwargs):
	    self.extra_context = {
	    	'title': "CHECKOUT FINAL",
	    	'token': self.request.GET.get('token')
	    }
	    self.kwargs.update(self.extra_context)
	    kwargs = self.kwargs
	    return super().get_context_data()

	def get_object(self):
		url = self.request.GET.get('token', False)
		if url is not False:
			print("Masuk URL")
			self.queryset = self.model.objects.get(token=url)
			# if self.queryset.status == 'pendding':
			return self.queryset
		else:
			self.queryset = None
			return self.queryset

	def get(self, *args, **kwargs):
		print("Get : ", self.queryset)
		if self.query_string:
			if self.request.GET.get('token', False) is False:
				return HttpResponseRedirect(reverse('paket:view'))
		try:
			ada_token = self.model.objects.get(token=self.request.GET.get('token', False))
		except Exception as e:
			return HttpResponseRedirect(reverse('paket:view'))
		return super().get(*args, **kwargs)

class DetailSuccess(ListView):
	model = modelTransaksi
	context_object_name = "object"
	template_name = 'transaksi/checkOut_success.html'
	query_string = True

	def get(self, *args, **kwargs):
		token = self.request.GET.get('token', False)
		try:
			trans = self.model.objects.get(token=token)
			trans.status = 'success'
			trans.save()
			print(trans)
		except Exception as e:
			return HttpResponseRedirect(reverse('paket:view'))

		return super().get(args, kwargs)
