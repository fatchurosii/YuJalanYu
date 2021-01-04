from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings
from .views import checkOut, DetailCheckOut, DetailTesting, DetailSuccess

app_name = 'transaksi'
urlpatterns = [
	re_path(r'^$', login_required(checkOut.as_view()), name='url_success'),
	re_path(r'^$', login_required(checkOut.as_view()), name='checkOut'),
	re_path(r'^final/$', login_required(DetailCheckOut.as_view()), name='final'),
	re_path(r'^testing/$', login_required(DetailTesting.as_view()), name='testing'),
	re_path(r'^success/$', login_required(DetailSuccess.as_view()), name='success')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)