from rest_framework import serializers
from .models import WebUser

class WebUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=4, max_length=20, required=True)
    password = serializers.CharField(min_length=4, max_length=20, required=True)

    class Meta:
        model = WebUser
        fields = ["username", "password"]

    def validate(self, data):
        if data['password'] != data['password']:
            raise serializers.ValidationError("Passwords don't match")
        if data['username'] != data['username']:
            raise serializers.ValidationError("Username doesn't match")
        return data