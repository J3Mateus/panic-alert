from django.db import models

from apps.common.models.base_model import BaseModel

class Educator(BaseModel):
    name = models.CharField()
    phone = models.CharField()
    whatsapp = models.CharField()
    email = models.EmailField()
    
    def __str__(self):
        return self.nome
    
    class Meta:
        app_label = 'educator'
        db_table  = f'{app_label}'