from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from .views import homeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView.as_view(), name='home'),
    path('user/', include('userManage.urls', namespace='akun')),
	path('paket/', include('Paket.urls', namespace='paket')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)