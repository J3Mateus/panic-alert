from django.db import models

from apps.common.models.base_model import BaseModel
from apps.counties.models import Counties
from apps.address.models import Address

class School(BaseModel):
    name = models.CharField(verbose_name='Nome da escola',max_length=500)
    address = models.ForeignKey(Address,verbose_name='Endereço da escola',on_delete=models.SET_NULL,related_name='address_school',null=True)
    responsible = models.ForeignKey('users.BaseUser', on_delete=models.CASCADE, related_name='responsible_schools')
    geolocation = models.CharField(verbose_name='Geolocalização da escola',max_length=500)
    countie = models.ForeignKey(Counties,verbose_name="Município da escola",null=True, blank=True, on_delete=models.SET_NULL, related_name='countie_school')
    created_by = models.ForeignKey('users.BaseUser', on_delete=models.CASCADE, related_name='created_schools')
    deleted_by = models.ForeignKey('users.BaseUser', on_delete=models.SET_NULL, related_name='deleted_schools', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'school'
        db_table  = f'{app_label}'