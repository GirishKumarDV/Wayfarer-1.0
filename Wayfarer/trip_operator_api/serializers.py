from rest_framework import serializers
from trip_operator.models import Trip,Operator

class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','op_name','op_email','op_phone')
        model = Operator
        

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','category','operator','location','duration','price','difficulty')
        model = Trip