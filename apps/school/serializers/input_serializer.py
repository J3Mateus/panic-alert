from rest_framework import serializers

class InputSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    responsible =  serializers.CharField(required=False)
    geolocation  = serializers.CharField(required=False)