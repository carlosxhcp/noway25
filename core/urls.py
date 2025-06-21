
from django.contrib import admin
from django.urls import path, include
from main_app.views import index
from main_app.views import shop
from django.conf import settings
from django.conf.urls.static import static
from main_app.views import perfil
from main_app.views import manifest
from main_app.views import lookbook
from main_app.views import deform
from main_app.views import fbd
from main_app.views import dadhat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', index,name='index'),
    path('shop', shop, name='shop'),
    path('perfil/', perfil, name='perfil'),
    path('manifest', manifest, name='manifest'),
    path('lookbook', lookbook, name='lookbook'),
    path('lookbook/deform/', deform, name='lookbook_deform'),
    path('lookbook/fuckbaddays/', fbd, name='lookbook_fbd'),
    path('lookbook/dadhat/', dadhat, name='lookbook_dadhat'),
    path('perfil/', include('main_app.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)