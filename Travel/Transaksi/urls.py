from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import checkOut, DetailCheckOut

app_name = 'transaksi'
urlpatterns = [
	re_path(r'^$', checkOut.as_view(), name='url_success'),
	re_path(r'^(?P<slug>[\w-]+)$', checkOut.as_view(), name='checkOut'),
	re_path(r'^final/$', DetailCheckOut.as_view(), name='final')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)