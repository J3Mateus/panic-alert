from rest_framework import serializers

class AddressInputSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    zipCode = serializers.CharField(required=True)
    district = serializers.CharField(required=True)
    uf = serializers.CharField(required=True)
    location = serializers.CharField(required=True)
    publicArea = serializers.CharField(required=True)