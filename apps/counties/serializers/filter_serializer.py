from rest_framework import serializers

class CountiesFilterSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    code = serializers.CharField(required=False, allow_null=True, default=None)