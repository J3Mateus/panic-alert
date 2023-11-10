from rest_framework import serializers
from apps.cop.serializers.output_serializer import COPOutputSerializer

from apps.school.serializers.output_serializer import SchoolOutputSerializer

class RolesOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    code = serializers.CharField()
    
class UserOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    full_name  = serializers.CharField(required=False)
    role       = serializers.SerializerMethodField(required=False)
    email      = serializers.CharField(required=False)
    phone      = serializers.CharField(required=False)
    school     = serializers.SerializerMethodField(required=False)
    cops        = serializers.SerializerMethodField(required=False)
    whatsapp   = serializers.CharField(required=False)
    is_deleted = serializers.BooleanField(required=False)
     
    def get_cops(self,obj):
        cop = obj.cop.all()
        return COPOutputSerializer(cop,many=True).data   
     
    def get_role(self,obj):
        roles = obj.role.all()
        return RolesOutputSerializer(roles,many=True).data
    
    def get_school(self, obj):
        # obj é a instância do modelo User que está sendo serializada
        schools = obj.school.all()  # Recupera todas as escolas associadas ao usuário
        return SchoolOutputSerializer(schools, many=True).data
    