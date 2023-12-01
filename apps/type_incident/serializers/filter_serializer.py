from rest_framework import serializers

class TypeIncidentFilterSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)    
    name = serializers.CharField(required=False)
    code = serializers.CharField(required=False)