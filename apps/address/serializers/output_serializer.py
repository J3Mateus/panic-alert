from rest_framework import serializers

class AddressOutputSerializer(serializers.Serializer):
    zipCode = serializers.CharField()
    district = serializers.CharField()
    uf = serializers.CharField()
    location = serializers.CharField()
    publicArea = serializers.CharField()