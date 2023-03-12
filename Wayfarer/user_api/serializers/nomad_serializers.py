from rest_framework import serializers
from user.models import Nomad
from django.contrib.auth.hashers import make_password


class NomadSerializer(serializers.ModelSerializer):
    nomad_pass = serializers.CharField(
    write_only=True,
    required=True,
    style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        fields = ('id','nomad_name','nomad_email','nomad_phone','nomad_pass','nomad_dp')
        model = Nomad
    validate_password = make_password