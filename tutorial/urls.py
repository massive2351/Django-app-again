from django.contrib import admin
from django.urls import path, include   #変更
from django.conf import settings #追加
from django.conf.urls.static import static #追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pdfmr/', include('pdfmr.urls')),
    path('', include('accounts.urls')), 
]
