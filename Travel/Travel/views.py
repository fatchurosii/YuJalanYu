from django.shortcuts import render
from django.views.generic import TemplateView
from Paket.models import modelPaket, imagesPaket
import datetime

class homeView(TemplateView):
	template_name = 'home.html'
	http_method_name = ['get']

	def get(self, request):
		model = modelPaket.objects.order_by('tgl_dibuat')
		data = []
		for x in model:
			if x.tgl_berangkat > datetime.date.today():
				data.append(x)
		modelImg = imagesPaket.objects.filter(id_paket=data[0])
		print()
		context = {
		'title':"HOME",
		'data':data,
		'img':modelImg
		}

		return render(self.request, self.template_name, context)