from rest_framework import generics
from trip_operator.models import *
from .serializers import *

# Create your views here.
class TripList(generics.ListCreateAPIView):
    queryset = Trip.tripobjects.all()
    serializer_class = TripSerializer
    pass

class TripDetail(generics.RetrieveDestroyAPIView):
    queryset = Trip.tripobjects.all()
    serializer_class = TripSerializer
    pass