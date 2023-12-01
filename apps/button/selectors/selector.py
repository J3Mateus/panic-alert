from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404
from apps.button.models import Button

from apps.button.filter import ButtonFilter

def button_get(id: str):
    try:
        return get_object_or_404(Button, id=id)
    except Http404:
       return None


def button_list(*, filters=None) -> QuerySet[Button]:
    filters = filters or {}

    qs = Button.objects.all()

    return ButtonFilter(filters, qs).qs
