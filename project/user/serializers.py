from rest_framework import serializers

from user.models import SignUp
# from django.contrib.auth import get_user_model

# User= get_user_model()

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields= ("__all__")

        
        
