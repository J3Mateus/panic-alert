from rest_framework import serializers

from apps.users.serializers.output_serializer import OutputSerializer as SerializerUser


class OutputSerializer(serializers.Serializer):
    id = serializers.CharField()
    responsible = SerializerUser()
    name = serializers.CharField()
    address = serializers.CharField()
    geolocation = serializers.CharField()
    is_deleted = serializers.BooleanField()
    created_by = SerializerUser()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()