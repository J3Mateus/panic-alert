from rest_framework import serializers

class TypeIncidentSerializer(serializers.Serializer):
    id   = serializers.UUIDField()
    name = serializers.CharField()
    code = serializers.CharField()