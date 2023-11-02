from typing import Optional

from django.db import transaction

from apps.common.services.common_update import model_update
from apps.users.models import BaseUser
from apps.users.selectors.user import user_get
from django.contrib.auth.hashers import make_password


def user_create(
    *, email: str,phone: str,
    whatsapp: str, 
    is_active: bool = True, 
    is_admin: bool = False,
    first_name: str, 
    last_name: str, 
    created_by: BaseUser,
    schools: [str],
    roles: [str],
    password: Optional[str] = None
) -> BaseUser:
    user = BaseUser.objects.create(email=email,phone=phone,whatsapp=whatsapp,
                                  first_name=first_name,last_name=last_name,
                                  created_by=created_by,is_active=is_active, 
                                  is_admin=is_admin,password=make_password(password))
    
    for school in schools:
        user.school.add(school)
    
    for role in roles:
        user.role.add(role)
            
    user.save()
    return user


@transaction.atomic
def user_update(*, user: BaseUser, data) -> BaseUser:
    non_side_effect_fields = ["first_name", "last_name"]

    user, has_updated = model_update(instance=user, fields=non_side_effect_fields, data=data)

    # Side-effect fields update here (e.g. username is generated based on first & last name)

    # ... some additional tasks with the user ...

    return user

@transaction.atomic
def user_delete(*,id:str) -> BaseUser:
    user: BaseUser = user_get(pk=id)
    user.full_clean()
    user.delete()

    return user
