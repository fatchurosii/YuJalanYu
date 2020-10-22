from django.shortcuts import render
from django.views.generic import ListView, DetailView
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
	    self.kwargs.update(self.extra_context)
	    print(imagesPaket.objects.all())
	    kwargs = self.kwargs
	    return super().get_context_data()

class DetailPaket(DetailView):
	model = modelPaket
	template_name = 'paket/detailPaket.html'
	extra_context = {
			'title':'DETAIL',
			'img_object': imagesPaket.objects.all(),
		}

	def get_context_data(self, *args, **kwargs):
	    self.kwargs.update(self.extra_context)
	    kwargs = self.kwargs
	    print(kwargs)
	    return super().get_context_data(*args, **kwargs)





