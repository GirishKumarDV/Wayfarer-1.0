from rest_framework import generics
from ..serializers import nomad_serializers
# Create your views here.

class NomadCreate(generics.CreateAPIView):
    serializer_class = nomad_serializers.NomadSerializer


