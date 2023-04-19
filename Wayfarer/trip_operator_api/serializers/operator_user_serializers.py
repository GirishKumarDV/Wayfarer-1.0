from rest_framework import serializers
from trip_operator.models import Operator,OperatorUser
from django.contrib.auth.hashers import make_password

class OperatorUserSerializer(serializers.ModelSerializer):
     user_pass = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        fields = ('id','user_name','user_email','user_phone','user_pass','operator')
        model = OperatorUser
    validate_password = make_password