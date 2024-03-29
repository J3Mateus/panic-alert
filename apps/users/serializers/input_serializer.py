from rest_framework import serializers

class UserCreateInputSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    schools = serializers.ListField(required=False)
    roles = serializers.ListField(required=True)
    cops  = serializers.ListField(required=False)
    whatsapp =  serializers.CharField(required=True)
    is_admin = serializers.BooleanField(required=False)
    full_name = serializers.CharField(required=True)
    password  = serializers.CharField(required=True)

class UserUpdateInputSerializer(serializers.Serializer):
    email = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    schools = serializers.ListField(required=False)
    roles = serializers.ListField(required=False)
    cops  = serializers.ListField(required=False)
    whatsapp =  serializers.CharField(required=False)
    is_admin = serializers.BooleanField(required=False)
    full_name = serializers.CharField(required=False)
    password  = serializers.CharField(required=False)