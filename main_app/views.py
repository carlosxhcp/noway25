from django.shortcuts import render
from allauth.account.forms import LoginForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import NewsletterSubscriber
from django.contrib.auth.decorators import login_required



# Create your views here.




def index(request):
    return render(request, 'index.html')



def shop(request):
    return render(request, 'shop.html')




@csrf_exempt  # se você não estiver usando CSRF token, mas depois podemos melhorar isso!
def inscrever_newsletter(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")

            if not email:
                return JsonResponse({"success": False, "error": "Email é obrigatório"}, status=400)

            # evita duplicidade
            subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)

            return JsonResponse({"success": True, "created": created})

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    return JsonResponse({"success": False, "error": "Método não permitido"}, status=405)

@login_required
def perfil(request):
    return render(request, 'perfil.html')


def manifest(request):
    return render(request, 'manifest.html')

def lookbook(request):
    return render(request, 'lookbook.html')