from django.db import transaction

from apps.address.models import Address

@transaction.atomic
def address_create(*,zipCode: str, district: str, uf: str,location: str, publicArea: str) -> Address:
    address =  Address(
        zipCode=zipCode,
        district=district,
        uf=uf,
        location=location,
        publicArea=publicArea
    )
    
    address.full_clean()
    address.save()
    
    return address