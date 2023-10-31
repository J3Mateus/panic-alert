from rest_framework import serializers

class BaseUserSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    first_name = serializers.CharField()
    last_name  = serializers.CharField()
    email      = serializers.CharField()
    phone      = serializers.CharField()
    whatsapp   = serializers.CharField()
    is_active  = serializers.BooleanField()
    is_admin   = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    
class SchoolOutputSerializer(serializers.Serializer):
    id = serializers.CharField()
    responsible  = BaseUserSerializer()
    name = serializers.CharField()
    address = serializers.CharField()
    geolocation = serializers.CharField()
    is_deleted = serializers.BooleanField()
    created_by = BaseUserSerializer()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()