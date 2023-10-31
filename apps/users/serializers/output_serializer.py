from rest_framework import serializers

from apps.school.serializers.output_serializer import SchoolOutputSerializer


class UserOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    first_name = serializers.CharField()
    last_name  = serializers.CharField()
    email      = serializers.CharField()
    phone      = serializers.CharField()
    school = serializers.SerializerMethodField()
    whatsapp   = serializers.CharField()
    is_active  = serializers.BooleanField()
    is_admin   = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    
    def get_school(self, obj):
        # obj é a instância do modelo User que está sendo serializada
        schools = obj.school.all()  # Recupera todas as escolas associadas ao usuário
        return SchoolOutputSerializer(schools, many=True).data
    