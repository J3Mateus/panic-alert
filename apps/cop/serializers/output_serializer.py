from rest_framework import serializers

class BaseUserSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    full_name  = serializers.SerializerMethodField()
    email      = serializers.CharField()
    phone      = serializers.CharField()
    is_active  = serializers.BooleanField()
    
    def get_full_name(self,obj):
        return obj.get_full_name()
    
class CountieOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    code = serializers.CharField()

class AddressOutputSerializer(serializers.Serializer):
    zipCode = serializers.CharField()
    district = serializers.CharField()
    uf = serializers.CharField()
    location = serializers.CharField()
    publicArea = serializers.CharField()
        
class COPOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    responsible  = BaseUserSerializer()
    name = serializers.CharField()
    address = AddressOutputSerializer()
    geolocation = serializers.CharField()
    countie    = CountieOutputSerializer()
    is_deleted = serializers.BooleanField()