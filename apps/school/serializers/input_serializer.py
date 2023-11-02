from rest_framework import serializers

class SchoolCreateInputSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    responsible =  serializers.CharField(required=True)
    geolocation  = serializers.CharField(required=True)

class SchoolUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    responsible =  serializers.CharField(required=False)
    geolocation  = serializers.CharField(required=False)