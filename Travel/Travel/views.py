from django.shortcuts import render
from django.views.generic import TemplateView, View
from Paket.models import modelPaket, imagesPaket
import datetime

class homeView(View):
	template_name = 'home.html'
	http_method_name = ['get']

	def get(self, request):
		model = modelPaket.objects.order_by('-tgl_dibuat')
<<<<<<< HEAD
		modelImg = imagesPaket.objects.all()
		data = modelImg.values('id_paket').distinct()
		
=======
		# model.images
>>>>>>> e82c826bb2cfdbb62b5e703bede8562e03e93732
		dataPaket = []
		dataImg = []
		for x in model:
			if x.tgl_berangkat > datetime.date.today():
				dataPaket.append(x)
<<<<<<< HEAD
=======
				# dataImg.append(imagesPaket.objects.get(id_paket=x))
>>>>>>> e82c826bb2cfdbb62b5e703bede8562e03e93732
		
		for x in modelImg.values('id_paket').distinct():
			print(x['id_paket'])
			oper = modelImg.filter(id_paket=x['id_paket'])
			dataImg.append(oper[0])
				
		print(dataImg)
		context = {
		'title':"HOME",
		'data':dataPaket,
		'img':dataImg
		}

		return render(self.request, self.template_name, context)