from django.db import transaction
from django.forms import ValidationError

from apps.common.services.common_update import model_update

from apps.users.models import BaseUser
from apps.cop.models import COP
from apps.button.models import Button
from apps.type_incident.models import Type_Incident

from apps.users.selectors.user import user_get

@transaction.atomic
def button_create(*,user: BaseUser) -> Button:
    try:
        user_instance = user_get(pk=user.pk)
        
        if user_instance is None:
            raise ValidationError("Usuário não encontrado.")

        school = user_instance.schools.first()

        if school is None:
            raise ValidationError("O usuário não está associado a nenhuma escola.")

        countie = school.countie
        cop = COP.objects.filter(countie=countie).first()
        type_incident = Type_Incident.objects.get(pk='228996cd-aef9-42e9-b1ef-08b89132a37d')

        button = Button(
            type_incident=type_incident,
            teacher=user_instance,
            school=school,
            cop=cop,
            countie=countie,
            status="ocorrencia_iniciada",
        )

        button.save()
        return button

    except Type_Incident.DoesNotExist:
        raise ValidationError("Type_Incident with specified ID not found.")

    except COP.DoesNotExist:
        raise ValidationError("COP not found for the associated countie.")

    except ValidationError as ve:
        raise ValidationError(ve.message)

@transaction.atomic
def button_update(*, button: Button, data) -> Button:
    non_side_effect_fields = ["type_incident","countie","concluded_by","updater_by","responsible","description","problem_solving","status"]

    new_button, has_updated = model_update(instance=button, fields=non_side_effect_fields, data=data)

    return new_button