from typing import Optional

from django.db import transaction
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password

from apps.common.services.common_update import model_update
from apps.users.exceptions import RoleNotFoundValidationError, SchoolNotFoundValidationError, UserNotFoundValidationError
from apps.users.models import BaseUser
from apps.role.models import Roles
from apps.school.models import School
from apps.users.selectors.user import user_get


@transaction.atomic
def user_create(
    *, email: str,phone: str,
    whatsapp: str, 
    is_active: bool = True, 
    is_admin: bool = False,
    first_name: str, 
    last_name: str, 
    created_by: BaseUser,
    schools: [str] = [],
    roles: [str],
    password: Optional[str] = None
) -> BaseUser:    
    user = BaseUser.objects.create(email=email,phone=phone,whatsapp=whatsapp,
                                  first_name=first_name,last_name=last_name,
                                  created_by=created_by,is_active=is_active, 
                                  is_admin=is_admin,password=make_password(password))
    
    for school_id in schools:
        try:
            school = School.objects.get(id=school_id)
            user.school.add(school)
        except ObjectDoesNotExist:
            raise SchoolNotFoundValidationError(f"A escola com o UUID({school_id}) fornecido não existe no banco de dados.",code='422')
    
    for role_id in roles:
        try:
            role = Roles.objects.get(id=role_id)
            user.role.add(role)
        except ObjectDoesNotExist:
            raise RoleNotFoundValidationError(f"O papel com o UUID({role_id})  fornecido não existe no banco de dados.",code='422')
            
    user.save()
    return user


@transaction.atomic
def user_update(*, user: BaseUser, data) -> BaseUser:
    non_side_effect_fields = ["first_name", "last_name","role","school","email","phone","whatsapp","is_deleted"]

    user, has_updated = model_update(instance=user, fields=non_side_effect_fields, data=data)

    # Side-effect fields update here (e.g. username is generated based on first & last name)

    # ... some additional tasks with the user ...

    return user

@transaction.atomic
def user_delete(*,id:str) -> BaseUser:
    user: BaseUser = user_get(pk=id)
    
    try:
        user = BaseUser.objects.get(id=id)
    except ObjectDoesNotExist:
        raise UserNotFoundValidationError(f"O usuário com o UUID({id}) fornecido não existe no banco de dados.",code='422')
        
    user.full_clean()
    user.delete()

    return user
