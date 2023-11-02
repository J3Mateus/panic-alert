from rest_framework import serializers

class BaseUserSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    full_name  = serializers.SerializerMethodField()
    email      = serializers.CharField()
    phone      = serializers.CharField()
    is_active  = serializers.BooleanField()
    
    def get_full_name(self,obj):
        
        return obj.get_full_name()
    
class SchoolOutputSerializer(serializers.Serializer):
    id = serializers.CharField()
    responsible  = BaseUserSerializer()
    name = serializers.CharField()
    address = serializers.CharField()
    geolocation = serializers.CharField()
    is_deleted = serializers.BooleanField()