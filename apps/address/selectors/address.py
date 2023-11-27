from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404
from requests import get as getFrom
from apps.address.models import Address
import re

def address_get_api(cep: str) -> Address:
    try:
       newCep = cep.strip()
       newCep = re.sub(r'\D', '', newCep)
       uriCEP = f'https://opencep.com/v1/{newCep}'
       response = getFrom(uriCEP)
       status_code = response.status_code
       json_response = response.json()
       if 'error' in json_response:
           raise ValueError("CEP inválido")

       if status_code != 200:
            raise ValueError("Erro no serviço externo")
        
       obj_address =  Address(
           zipCode=json_response.get("cep"),
           district=json_response.get("bairro",""),
           uf=json_response.get("uf",""),
           location=json_response.get("localidade",""),
           publicArea=json_response.get("logradouro","")
       )
       return obj_address
    except ValueError as ve:
        return None