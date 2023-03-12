
from rest_framework import generics
from rest_framework.response import Response
from trip_operator.models import Operator,Trip
from ..serializers.operator_serializers import OperatorSerializer
from ..serializers.trip_serializers import TripSerializer
# Create your views here.

# url /operator/api/createop
class OperatorCreate(generics.CreateAPIView):
    serializer_class = OperatorSerializer
    
#url /operator/api/listoptrips/<pk>
class OperatorDetail(generics.ListAPIView):
    serializer_class = TripSerializer
    def get(self,request,pk):
        queryset = Trip.tripobjects.filter(operator=pk).all()
        data = {}
        for item in queryset:
            trip_data = {}
            trip_data['category'] = item.category.name
            trip_data['location'] = item.location
            data[f'{item.id}']=trip_data
        return Response(data)    

class OperatorTripCreate(generics.CreateAPIView):
    serializer_class = TripSerializer
    

class OperatorView(generics.ListAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer

class OperatorDelete(generics.RetrieveDestroyAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer
