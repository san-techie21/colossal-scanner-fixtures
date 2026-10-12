from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Account


@require_POST
def transfer(request):
    Account.transfer(request.user, request.POST["to"], request.POST["amount"])
    return JsonResponse({"ok": True})
