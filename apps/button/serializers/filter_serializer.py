from rest_framework import serializers

class ButtonFilterSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    type_incident = serializers.UUIDField(required=False)
    teacher  = serializers.UUIDField(required=False)
    concluded_by  = serializers.UUIDField(required=False)
    updater_by  = serializers.UUIDField(required=False)
    school  = serializers.UUIDField(required=False)
    cop = serializers.UUIDField(required=False)
    responsible = serializers.UUIDField(required=False)
    status = serializers.CharField(required=False)
    countie =  serializers.UUIDField(required=False)