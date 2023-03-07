from rest_framework import generics
from trip_operator.models import Trip
from ..serializers.trip_serializers import TripSerializer

# Create your views here.
class TripList(generics.ListCreateAPIView):
    queryset = Trip.tripobjects.all()
    serializer_class = TripSerializer
    pass

class TripDetail(generics.RetrieveDestroyAPIView):
    queryset = Trip.tripobjects.all()
    serializer_class = TripSerializer
    pass