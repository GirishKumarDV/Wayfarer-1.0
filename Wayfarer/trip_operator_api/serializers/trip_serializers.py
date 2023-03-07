from rest_framework import serializers
from trip_operator.models import Trip

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','category','operator','location','duration','price','difficulty')
        model = Trip