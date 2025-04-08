
from django.contrib import admin
from django.urls import path, include
from main_app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', index,name='index')
]
