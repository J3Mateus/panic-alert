from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404
from apps.cop.models import COP

from apps.cop.filter import CopFilter

def cop_get(cop: COP, id: str):
    try:
        return get_object_or_404(COP, id=id)
    except Http404:
       return None


def cop_list(*, filters=None) -> QuerySet[COP]:
    filters = filters or {}

    qs = COP.objects.all()

    return CopFilter(filters, qs).qs
