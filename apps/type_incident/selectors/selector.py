from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404

from apps.type_incident.models import Type_Incident
from apps.type_incident.filters import TypeIncidentFilter

def type_incident_get(type_incident: Type_Incident, id: str):
    try:
        return get_object_or_404(type_incident, id=id)
    except Http404:
       return None


def type_incident_list(*, filters=None) -> QuerySet[Type_Incident]:
    filters = filters or {}

    qs = Type_Incident.objects.all()

    return TypeIncidentFilter(filters, qs).qs
