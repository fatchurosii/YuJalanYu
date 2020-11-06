from django.shortcuts import render
from django.views.generic import TemplateView, View
from Paket.models import modelPaket, imagesPaket
import datetime

class homeView(View):
	template_name = 'home.html'
	http_method_name = ['get']

	def get(self, request):
		model = modelPaket.objects.order_by('-tgl_dibuat')
		# model.images
		dataPaket = []
		dataImg = []
		for x in model:
			if x.tgl_berangkat > datetime.date.today():
				dataPaket.append(x)
				# dataImg.append(imagesPaket.objects.get(id_paket=x))
		
		context = {
		'title':"HOME",
		'data':dataPaket,
		'img':dataImg
		}

		return render(self.request, self.template_name, context)