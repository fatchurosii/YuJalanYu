from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import modelPaket, imagesPaket

# Create your views here.
class ListPaket(ListView):
	model = modelPaket
	template_name = 'paket/viewPaket.html'
	context_object_name = 'paket_object'
	extra_context = {
			'title':'PAKET TRAVEL',
			'img_object': imagesPaket.objects.all()
			}

	def get_context_data(self, **kwargs):
		data = modelPaket.objects.all()
		print(data[2].images)
		self.kwargs.update(self.extra_context)
		kwargs = self.kwargs
		return super().get_context_data()

class SearchPaket(ListView):
	template_name = 'paket/search.html'
	model = modelPaket
	extra_context = {
		'title':'Search',
		'error':None,
		'img':imagesPaket.objects.all()
	}
	query_string = True

	def get_queryset(self):
		url = self.request.GET.get('search', False)
		if url != False:
			data = self.model.objects.filter(
				Q(nama_paket__icontains=self.request.GET['search'])| 
				Q(destinasi__icontains=self.request.GET['search'])
				)
			if not data:
				self.extra_context = {
					'title':'Search',
					'error':"Data Tidak diTemukan"
				}
				self.queryset = None
				return self.queryset
			else:
				return data
		else:
			print("Masuk sebagai False")
			self.query_string = False
				

	def get(self, *args, **kwargs):
		if self.request.GET.get('search', False) is False:
			return HttpResponseRedirect(reverse('paket:view'))
		return super().get(self.request, *args, **kwargs)



class DetailPaket(DetailView):
	model = modelPaket
	template_name = 'paket/detailPaket.html'
	extra_context = None

	def get_context_data(self, *args, **kwargs):
		data = self.get_object()
		header = imagesPaket.objects.filter(id_paket=data.id)
		self.extra_context = {
			'title':'DETAIL',
			'header': header.get(id=header[0].id),
			'img': imagesPaket.objects.filter(id_paket=data.id)
		}
		self.kwargs.update(self.extra_context)
		kwargs = self.kwargs
		return super().get_context_data(*args, **kwargs)





