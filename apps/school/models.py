from django.db import models

from apps.common.models.base_model import BaseModel
#from apps.users.models import BaseUser

class School(BaseModel):
    name = models.CharField(verbose_name='Nome da escola',max_length=500)
    address = models.CharField(verbose_name='Endereço da escola',max_length=500)
    responsible = models.ForeignKey('users.BaseUser', on_delete=models.CASCADE, related_name='responsible_schools')
    geolocation = models.CharField(verbose_name='Geolocalização da escola',max_length=500)
    created_by = models.ForeignKey('users.BaseUser', on_delete=models.CASCADE, related_name='created_schools')
    deleted_by = models.ForeignKey('users.BaseUser', on_delete=models.CASCADE, related_name='deleted_schools', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'school'
        db_table  = f'{app_label}'