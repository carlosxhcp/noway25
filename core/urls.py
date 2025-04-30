
from django.contrib import admin
from django.urls import path, include
from main_app.views import index
from main_app.views import shop
from django.conf import settings
from django.conf.urls.static import static
from main_app.views import perfil
from main_app.views import manifest
from main_app.views import lookbook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', index,name='index'),
    path('shop', shop, name='shop'),
    path('perfil/', perfil, name='perfil'),
    path('manifest', manifest, name='manifest'),
    path('lookbook', lookbook, name='lookbook')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])