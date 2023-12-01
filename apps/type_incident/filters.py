import django_filters

from apps.type_incident.models import Type_Incident


class TypeIncidentFilter(django_filters.FilterSet):
    class Meta:
        model = Type_Incident
        fields = ("id", "name")