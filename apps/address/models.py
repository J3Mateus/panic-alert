from django.db import models
from apps.common.models.base_model import BaseModel

# Create your models here.
class Address(BaseModel):
    zipCode = models.CharField(verbose_name="CEP",max_length=10)
    district = models.CharField(verbose_name="Bairro",max_length=150)
    uf = models.CharField(verbose_name="Sigla do estado",max_length=2)
    location = models.CharField(verbose_name="Localidade",max_length=100,null=True)
    publicArea = models.CharField(verbose_name="Logradouro",max_length=250)
    
    def __str__(self):
        return self.zipCode

    class Meta:
        app_label = 'address'
        db_table  = f'{app_label}'