from django.db import transaction


from apps.common.services.common_update import model_update

from apps.cop.models import COP
from apps.address.models import Address
from apps.counties.selectors.counties import countie_get
from apps.users.models import BaseUser

from apps.cop.selectors.selector import cop_get
from apps.users.selectors.user import user_get

@transaction.atomic
def cop_create(*,name: str,address: Address,responsible: str,geolocation: str,countie: str,user: BaseUser) -> COP:
    address,created = Address.objects.get_or_create(**address)
    responsible = user_get(pk=responsible)
    countie = countie_get(id=countie)
    cop = COP(name=name,
              address=address,
              responsible=responsible,
              geolocation=geolocation,
              countie=countie,
              created_by=user)
    cop.full_clean()
    cop.save()
    return cop

@transaction.atomic
def cop_update(*,cop: COP, data: dict) -> COP:
    fields = ['name', 'address','responsible',"geolocation","is_deleted","countie"]
    
    if 'address' in data:
        address_data = {
        key: data['address'].get(key) for key in ["zipCode", "district", "uf", "location", "publicArea"]
        }    
        address, created = Address.objects.get_or_create(**address_data)
        data['address']= str(address.pk)  
        
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