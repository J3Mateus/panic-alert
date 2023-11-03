from django.db import transaction


from apps.common.services.common_update import model_update

from apps.cop.models import COP
from apps.users.models import BaseUser

from apps.cop.selectors.selector import cop_get
from apps.users.selectors.user import user_get

@transaction.atomic
def cop_create(*,name: str,address: str,responsible: str,geolocation: str,user: BaseUser) -> COP:
    responsible = user_get(pk=responsible)
    cop = COP(name=name,
              address=address,
              responsible=responsible,
              geolocation=geolocation,
              created_by=user)
    cop.full_clean()
    cop.save()
    return cop

@transaction.atomic
def cop_update(*,cop: COP, data: dict) -> COP:
    fields = ['name', 'address','responsible',"geolocation","is_deleted"]
    cop, has_updated = model_update(instance=cop, fields=fields, data=data)
    
    return cop

@transaction.atomic
def cop_delete(*,id:str) -> COP:
    cop = cop_get(cop=COP, id=id)
    if cop is None:
        return cop
    
    cop.full_clean()
    cop.delete()
    return cop