from rest_framework import permissions, viewsets

from .models import Statement
from .serializers import StatementSerializer


class StatementViewSet(viewsets.ModelViewSet):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer
    permission_classes = [permissions.IsAuthenticated]
