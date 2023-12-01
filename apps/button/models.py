from django.db import models

from apps.common.models.base_model import BaseModel
from apps.school.models import School
from apps.cop.models import COP
from apps.type_incident.models import Type_Incident

class Button(BaseModel):
    STATUS_CHOICES = (
        ('ajuda_caminho', 'Ajuda a Caminho'),
        ('ocorrencia_resolvida', 'Ocorrência Resolvida'),
        ('ocorrencia_iniciada', 'Ocorrência iniciada'),
        # Adicione outros status conforme necessário
    )

    type_incident = models.ForeignKey(Type_Incident, on_delete=models.SET_NULL, related_name='type_incident_button', null=True)
    teacher = models.ForeignKey('users.BaseUser', on_delete=models.SET_NULL, related_name='teacher_button', null=True)
    concluded_by = models.ForeignKey('users.BaseUser', on_delete=models.SET_NULL, related_name='concluded_by_button', null=True)
    updater_by = models.ForeignKey('users.BaseUser', on_delete=models.SET_NULL, related_name='updater_by_button', null=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, related_name='school_button', null=True)
    cop = models.ForeignKey(COP, on_delete=models.SET_NULL, related_name='cop_button', null=True)
    responsible = models.ForeignKey('users.BaseUser', on_delete=models.SET_NULL, related_name='responsible_button', null=True,default=None)
    description = models.TextField(verbose_name='Descrição do alerta', null=True,default='')
    problem_solving = models.TextField(verbose_name='Resolução do problema', max_length=500,null=True,default='')    
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    
    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'button'
        db_table  = f'{app_label}'