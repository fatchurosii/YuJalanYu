from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from .models import modelTransaksi
from Paket.models import modelPaket

# Create your views here.
class checkOut(DetailView):
	model = modelPaket
	template_name = 'transaksi/checkOut.html'
	extra_context = None
	query_string = True


	def get_context_data(self, **kwargs):
		print(self.get_object())
		data = modelPaket.objects.get(slug=self.request.GET.get('slug'))
		# print(data)
		self.extra_context = {
		'title':'CheckOut',
		'data': "data"
		}
		self.kwargs.update(self.extra_context)
		kwargs = self.kwargs
		return super().get_context_data()