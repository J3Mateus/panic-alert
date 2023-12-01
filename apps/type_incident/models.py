from django.db import models
from apps.common.models.base_model import BaseModel

class Type_Incident(BaseModel):
    TYPE_INCIDENT = [
        ('nao_informado', "Não informado"),
        ('incendio', 'Incêndio'),
        ('briga', 'Briga'),
        ('invasao_armada', 'Invasão Armada'),
    ]

    INCENDIO_CODE = "incendio"
    BRIGA_CODE = "briga"
    INVASAO_ARMADA_CODE = "invasao_armada"
    NAO_INFORMADO_CODE = "nao_informado"

    name = models.CharField(max_length=20, choices=TYPE_INCIDENT)
    code = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'type_incident'
        db_table = f'{app_label}'
