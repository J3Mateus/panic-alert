from collections.abc import Iterable
from django.db import models
import secrets
from apps.common.models.base_model import BaseModel

class Counties(BaseModel):
    name = models.CharField(verbose_name='Nome do município',max_length=500)
    code = models.CharField(verbose_name='Código unico',max_length=500)
    released = models.BooleanField(verbose_name='Cidade liberada',default=False)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = secrets.token_hex(4)
            
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'counties'
        db_table  = f'{app_label}'