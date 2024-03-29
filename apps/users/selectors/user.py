from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404

from apps.users.filters import BaseUserFilter
from apps.users.models import BaseUser

def get_user_by_email(*,email:str) -> BaseUser:
    try:
        return get_object_or_404(BaseUser, email=email)
    except Http404:
       return None
   
def user_get_login_data(*, user: BaseUser):
    try:
        return get_object_or_404(BaseUser, id=user.id)
    except Http404:
       return None

def user_get(*,pk: str) -> BaseUser | None:
    try:
        return get_object_or_404(BaseUser, id=pk)
    except Http404:
       return None
    

def user_list(*, filters=None) -> QuerySet[BaseUser]:
    filters = filters or {}

    qs = BaseUser.objects.all()

    return BaseUserFilter(filters, qs).qs
