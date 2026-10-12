from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from .models import Statement


class StatementDelete(LoginRequiredMixin, View):
    def post(self, request, pk):
        statement = get_object_or_404(Statement, pk=pk)
        statement.delete()
        return redirect("/statements/")
