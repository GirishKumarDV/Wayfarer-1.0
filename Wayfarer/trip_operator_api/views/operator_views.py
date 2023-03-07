from rest_framework import generics
from trip_operator.models import Operator,Trip
from ..serializers.operator_serializers import OperatorSerializer
from ..serializers.trip_serializers import TripSerializer
# Create your views here.
class OperatorCreate(generics.CreateAPIView):
    serializer_class = OperatorSerializer
    

class OperatorDetail(generics.ListAPIView):
    serializer_class = TripSerializer
    def get_queryset(self):
        queryset = Trip.tripobjects.all()
        op_id = self.request.query_params.get('op_id')
        print(op_id)
        if op_id is not None:
            queryset = queryset.filter(operator=op_id)
        print(queryset)
        return queryset
    

class OperatorView(generics.ListAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer

class OperatorDelete(generics.RetrieveDestroyAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer
