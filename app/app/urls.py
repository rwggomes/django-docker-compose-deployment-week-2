from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static  
from django.http import HttpResponse

# Quick home view
def home(request):
    return HttpResponse("<h1>Você é um gênio e tá tudo funcionando!</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # <-- This handles the root path
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
