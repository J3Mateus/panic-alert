from rest_framework import serializers

class UserInputSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    schools = serializers.ListField(required=True)
    whatsapp =  serializers.CharField(required=True)
    is_admin = serializers.BooleanField(required=False)
    first_name = serializers.CharField(required=True)
    last_name =  serializers.CharField(required=True)
    password  = serializers.CharField(required=True)