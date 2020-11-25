from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import checkOut

app_name = 'transaksi'
urlpatterns = [
	re_path(r'^(?P<slug>[\w-]+)$', checkOut.as_view(), name='checkOut'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)