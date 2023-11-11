from typing import Optional
from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404
from apps.counties.models import Counties

from apps.counties.filter import CountieFilter

def countie_get(id: str):
    try:
        return get_object_or_404(Counties, id=id)
    except Http404:
       return None


def countie_list(*, filters=None) -> QuerySet[Counties]:
    filters = filters or {}

    qs = Counties.objects.all()

    return CountieFilter(filters, qs).qs
