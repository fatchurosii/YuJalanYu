from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import (ListPaket, DetailPaket, SearchPaket)

app_name='paket'
urlpatterns = [
		re_path(r'^$', ListPaket.as_view(), name='view'),
		re_path(r'^search/', SearchPaket.as_view(), name='search'),
		re_path(r'^detail/(?P<slug>[\w-]+)$', DetailPaket.as_view(), name='detail'),
	]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
