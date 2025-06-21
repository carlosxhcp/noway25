from django.urls import path
from main_app.views import inscrever_newsletter
from main_app.views import shop

urlpatterns = [
    path('inscrever/', inscrever_newsletter, name='inscrever_newsletter'),
]
