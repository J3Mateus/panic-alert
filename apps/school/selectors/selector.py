from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from apps.school.models import School

from apps.school.filter import SchoolFilter

def school_get(school: School, id: str):
    try:
        return get_object_or_404(School, id=id)
    except Http404:
       return None


def school_list(*, filters=None) -> QuerySet[School]:
    filters = filters or {}

    qs = School.objects.all()

    return SchoolFilter(filters, qs).qs
