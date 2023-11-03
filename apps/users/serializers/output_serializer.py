from rest_framework import serializers
from apps.cop.serializers.output_serializer import COPOutputSerializer

from apps.school.serializers.output_serializer import SchoolOutputSerializer

class RolesOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    code = serializers.CharField()
    
class UserOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    full_name  = serializers.SerializerMethodField()
    role       = serializers.SerializerMethodField()
    email      = serializers.CharField()
    phone      = serializers.CharField()
    school     = serializers.SerializerMethodField()
    cops        = serializers.SerializerMethodField()
    whatsapp   = serializers.CharField()
    is_deleted = serializers.BooleanField()
    
    def get_full_name(self,obj):
        return obj.get_full_name()
    
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
    