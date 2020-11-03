from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from .views import (Login, Logout)

app_name='akun'

urlpatterns = [
	re_path(r'^login/$', Login.as_view(), name='login'),
	re_path(r'^logout/$', Logout.as_view(), name='logout'),
]
