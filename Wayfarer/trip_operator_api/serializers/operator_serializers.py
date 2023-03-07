from rest_framework import serializers
from trip_operator.models import Operator
from django.contrib.auth.hashers import make_password


class OperatorSerializer(serializers.ModelSerializer):
    op_pass = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        fields = ('id','op_name','op_email','op_phone','op_pass')
        model = Operator
    validate_password = make_password
        