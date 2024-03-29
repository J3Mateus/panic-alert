from rest_framework import serializers

class UserFilterSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    is_admin = serializers.BooleanField(required=False, allow_null=True, default=None)
    is_deleted = serializers.BooleanField(required=False, allow_null=True, default=None)
    email = serializers.EmailField(required=False)