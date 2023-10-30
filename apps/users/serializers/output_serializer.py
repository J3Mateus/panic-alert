from rest_framework import serializers
from apps.users.models import BaseUser

class OutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ("id","first_name","last_name","email", "is_admin")