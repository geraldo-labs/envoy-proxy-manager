import base64


from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from rest_framework import status, viewsets

from host.models import Host
from host.serializers import HostSerializer

class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer
