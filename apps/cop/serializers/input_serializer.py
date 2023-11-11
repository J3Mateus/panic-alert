from rest_framework import serializers

class COPCreateInputSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    responsible =  serializers.CharField(required=True)
    countie    = serializers.UUIDField(required=True)
    geolocation  = serializers.CharField(required=True)

class COPUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    responsible =  serializers.CharField(required=False)
    is_deleted = serializers.BooleanField(required=False)
    geolocation  = serializers.CharField(required=False)
    countie    = serializers.UUIDField(required=False)