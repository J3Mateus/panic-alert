from rest_framework import serializers

class COPFilterSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    responsible = serializers.UUIDField(required=False, allow_null=True, default=None)
    created_by  = serializers.UUIDField(required=False, allow_null=True, default=None)
    deleted_by  = serializers.UUIDField(required=False, allow_null=True, default=None)
    is_deleted  = serializers.BooleanField(required=False)