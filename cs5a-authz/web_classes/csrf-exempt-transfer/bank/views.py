from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Account


@csrf_exempt
def transfer(request):
    if request.method == "POST":
        Account.transfer(request.user, request.POST["to"], request.POST["amount"])
    return JsonResponse({"ok": True})
