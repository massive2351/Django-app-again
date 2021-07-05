from django.contrib import admin
from django.urls import path, include   #変更

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pdfmr/', include('pdfmr.urls')),
    path('', include('accounts.urls')), 
]
