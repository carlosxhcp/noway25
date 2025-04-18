from django.urls import path
from main_app.views import inscrever_newsletter

urlpatterns = [
    # outras rotas...
    path('inscrever/', inscrever_newsletter, name='inscrever_newsletter'),
]
