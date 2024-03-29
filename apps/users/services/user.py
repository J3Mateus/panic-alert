from typing import Optional

from django.db import transaction
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password

from apps.common.services.common_update import model_update
from apps.cop.models import COP
from apps.users.exceptions import COPNotFoundValidationError, RoleNotFoundValidationError, SchoolNotFoundValidationError, UserNotFoundValidationError
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
    full_name: str, 
    created_by: BaseUser,
    schools: Optional[str] = [],
    roles: [str],
    cops:Optional[str] = [],
    password: Optional[str] = None
) -> BaseUser:    
    user = BaseUser.objects.create(email=email,phone=phone,whatsapp=whatsapp,
                                  full_name=full_name,
                                  created_by=created_by,is_active=is_active, 
                                  is_admin=is_admin,password=make_password(password))
    
    for school_id in schools:
        try:
            school = School.objects.get(id=school_id)
            user.schools.add(school)
        except ObjectDoesNotExist:
            raise SchoolNotFoundValidationError(f"A escola com o UUID({school_id}) fornecido não existe no banco de dados.",code='422')
    
    for role_id in roles:
        try:
            role = Roles.objects.get(id=role_id)
            user.roles.add(role)
        except ObjectDoesNotExist:
            raise RoleNotFoundValidationError(f"O papel com o UUID({role_id})  fornecido não existe no banco de dados.",code='422')
   
    for cops_id in cops:
        try:
            cop = COP.objects.get(id=cops_id)
            user.cops.add(cop)
        except ObjectDoesNotExist:
            raise COPNotFoundValidationError(f"A delegacia com o UUID({cops_id})  fornecido não existe no banco de dados.",code='422')
                
    user.save()
    return user


@transaction.atomic
def user_update(*, user: BaseUser, data) -> BaseUser:
    non_side_effect_fields = ["full_name","roles","schools","cops","email","phone","whatsapp","  "]

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
        
    user.delete()

    return user
