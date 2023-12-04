from rest_framework import serializers

class ButtonUpdateInputSerializer(serializers.Serializer):
    type_incident = serializers.UUIDField(required=False)
    concluded_by  = serializers.UUIDField(required=False)
    updater_by  = serializers.UUIDField(required=False)
    responsible = serializers.UUIDField(required=False)
    status = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    problem_solving = serializers.CharField(required=False)