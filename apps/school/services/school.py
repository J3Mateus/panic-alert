from django.db import transaction


from apps.common.services.common_update import model_update

from apps.school.models import School
from apps.users.models import BaseUser

from apps.school.selectors.selector import school_get
from apps.users.selectors.user import user_get

def school_create(*,name: str,address: str,responsible: str,geolocation: str,user: BaseUser) -> School:
    responsible = user_get(pk=responsible)
    school = School(name=name,
                    address=address,
                    responsible=responsible,
                    geolocation=geolocation,
                    created_by=user)
    school.full_clean()
    school.save()
    return school

@transaction.atomic
def school_update(*,school: School, data: dict) -> School:
    fields = ['name', 'address','responsible',"geolocation"]
    school, has_updated = model_update(instance=school, fields=fields, data=data)
    
    return school , has_updated

@transaction.atomic
def school_delete(*,id:str) -> School:
    school = school_get(school=School, id=id)
    if school is None:
        return school
    
    school.full_clean()
    school.delete()
    
    return school