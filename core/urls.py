
from django.contrib import admin
from django.urls import path, include
from main_app.views import index
from main_app.views import shop
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', index,name='index'),
    path('shop', shop, name='shop')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])