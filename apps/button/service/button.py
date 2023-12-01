from django.db import transaction
from django.forms import ValidationError

from apps.common.services.common_update import model_update

from apps.school.models import School
from apps.users.models import BaseUser
from apps.cop.models import COP
from apps.button.models import Button
from apps.counties.models import Counties
from apps.type_incident.models import Type_Incident

from apps.school.selectors.selector import school_get
from apps.users.selectors.user import user_get
from apps.cop.selectors.selector import cop_get

def button_create(*,user: BaseUser) -> Button:
    try:
        user_instance = user_get(pk=user.pk)
        
        if user_instance is None:
            raise ValidationError("User not found.")

        school = user_instance.schools.first()

        if school is None:
            raise ValidationError("User is not associated with any school.")

        countie = school.countie
        cop = COP.objects.filter(countie=countie).first()
        type_incident = Type_Incident.objects.get(pk='228996cd-aef9-42e9-b1ef-08b89132a37d')

        button = Button(
            type_incident=type_incident,
            teacher=user_instance,
            school=school,
            cop=cop,
            status="Ocorrência iniciada",
        )

        button.save()
        return button

    except Type_Incident.DoesNotExist:
        raise ValidationError("Type_Incident with specified ID not found.")

    except COP.DoesNotExist:
        raise ValidationError("COP not found for the associated countie.")

    except ValidationError as ve:
        # Handle validation errors, log them, or re-raise as needed
        print(f"Validation Error: {ve}")
        return None
