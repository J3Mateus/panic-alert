from django.db import models

from apps.common.models.base_model import BaseModel
from apps.counties.models import Counties
from apps.address.models import Address

class COP(BaseModel):
    name = models.CharField(verbose_name='Nome da delegacia',max_length=500)
    address = models.ForeignKey(Address,verbose_name='Endereço da delegacia',on_delete=models.SET_NULL,related_name='address_cop',null=True)
    responsible = models.ForeignKey('users.BaseUser', on_delete=models.CASCADE, related_name='responsible_cop')
    geolocation = models.CharField(verbose_name='Geolocalização da delegacia',max_length=500)
    created_by = models.ForeignKey('users.BaseUser', on_delete=models.CASCADE, related_name='created_cop')
    deleted_by = models.ForeignKey('users.BaseUser', on_delete=models.CASCADE, related_name='deleted_cop', null=True, blank=True)
    countie = models.ForeignKey(Counties,verbose_name="Município da policia",null=True, blank=True, on_delete=models.SET_NULL, related_name='countie_cops')
    
    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'cop'
        db_table  = f'{app_label}'