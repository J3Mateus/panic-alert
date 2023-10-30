from drf_yasg import openapi

from apps.docs.authentication.me.dto_response import DTO_VALIDATION_ERRO_ME
from apps.docs.school.dto_response import DTO_RESPONSE_DETAIL_BAD_REQUEST, DTO_RESPONSE_DETAIL_SCHOOL, DTO_RESPONSE_GET_ALL_SCHOOL

RESPONSE_SCHOOL_LIST = {
     200: openapi.Response(description='Informações das escolas obtidas com sucesso.',examples={
          'application/json':DTO_RESPONSE_GET_ALL_SCHOOL
         }),
     403: openapi.Response(description='Acesso não autorizado. O usuário não tem permissão para realizar esta operação.', examples={
            'application/json':DTO_VALIDATION_ERRO_ME,
     })
}

RESPONSE_SCHOOL_DETAIL = {
     200: openapi.Response(description='Informação da escola obtidas com sucesso.',examples={
          'application/json':DTO_RESPONSE_DETAIL_SCHOOL
         }),
     400:openapi.Response(description='Erro de Validação.',examples={
          'application/json':DTO_RESPONSE_DETAIL_BAD_REQUEST
         }),
     403: openapi.Response(description='Acesso não autorizado. O usuário não tem permissão para realizar esta operação.', examples={
            'application/json':DTO_VALIDATION_ERRO_ME,
     }),
     404: openapi.Response(description='Objeto não existente na base de dados.')
}