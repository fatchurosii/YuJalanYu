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
	template_name = 'transaksi/checkOut.html'
	query_string = True
	# context_object_name = 'paket_object'

	# def get_context_data(self, **kwargs):
	# 	data = modelPaket.objects.get(slug=self.kwargs['slug'])
	# 	extra_context = {
	# 		'title': 'CheckOut',
	# 		'data': data
	# 	}
	# 	self.kwargs.update(extra_context)
	# 	kwargs = self.kwargs
	# 	return super().get_context_data(**kwargs)

	# def get(self, request): 
	# 	print("Get")
	# 	print(self.request.GET.get('paket', False))
	# 	return self.post(self.request)

	def post(self, request):
		if request.POST.get('csrfmiddlewaretoken', False) is not False:
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
				"credit_card": {
					"secure": True
				}}
			print(param)
			token = snap.create_transaction(param)
			print("request : ", request.POST)
			print("token : ", token)

			data = self.form_class({'paket': paket, 'user': user, 'jumlah': jumlah,
									'totalHarga': (jumlah * paket.harga), 'token': token['token'], 'status': 'pendding'})
			data.save()
			# print(data['token'].data)
			return HttpResponseRedirect("%s?token={}".format(data['token'].data) % (reverse('transaksi:final')))
		else:
			print("false")
			return HttpResponseRedirect(reverse('paket:view'))

		
		

class DetailCheckOut(DetailView):
	model = modelTransaksi
	context_object_name = "object"
	template_name = 'transaksi/checkOut_Final.html'
	extra_context = None
	pk_url_kwarg = 'token'
	query_string = True

	def get_context_data(self, *args,**kwargs):
	    self.extra_context = {
	    	'title': "CHECKOUT FINAL",
	    	'token': self.request.GET.get('token')
	    }
	    print(self.extra_context)
	    self.kwargs.update(self.extra_context)
	    kwargs = self.kwargs
	    return super().get_context_data()

	def get_object(self):
		url = self.request.GET.get('token', False)
		print(url)
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
