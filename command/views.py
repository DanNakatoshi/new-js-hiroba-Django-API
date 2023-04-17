from .models import Command
from .serializers import CommandSerializer
from rest_framework import viewsets

class CommandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Command.objects.all().order_by('-date')
    serializer_class = CommandSerializer

