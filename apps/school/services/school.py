from django.db import transaction
from apps.address.models import Address

from apps.common.services.common_update import model_update
from apps.counties.selectors.counties import countie_get

from apps.school.models import School
from apps.users.models import BaseUser

from apps.school.selectors.selector import school_get
from apps.users.selectors.user import user_get

def school_create(*,name: str,responsible: str,geolocation: str,countie: str,user: BaseUser,address: Address) -> School:
    address,create = Address.objects.get_or_create(**address)
    responsible = user_get(pk=responsible)
    countie = countie_get(id=countie)
    school = School(name=name,
                    address=address,
                    responsible=responsible,
                    geolocation=geolocation,
                    created_by=user,
                    countie=countie)
    school.full_clean()
    school.save()
    return school

@transaction.atomic
def school_update(*,school: School, data: dict) -> School:
    fields = ['name', 'address','responsible',"geolocation","is_deleted","countie"]
    
    if 'address' in data:
        address_data = {
            key: data['address'].get(key) for key in ["zipCode", "district", "uf", "location", "publicArea"]
        }    
        address, created = Address.objects.get_or_create(**address_data)
        data['address']= str(address.pk)  
                                                    
    new_school, has_updated = model_update(instance=school, fields=fields, data=data)
    return new_school

@transaction.atomic
def school_delete(*,id:str) -> School:
    school = school_get(school=School, id=id)
    if school is None:
        return school
    
    school.full_clean()
    school.delete()
    
    return school