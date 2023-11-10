import uuid
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')
    is_deleted = models.BooleanField(default=False, verbose_name='Excluído', db_index=True)
    
    class Meta:
        abstract = True
    
    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()
    
    def undelete(self):
        self.is_deleted = False
        self.save()
