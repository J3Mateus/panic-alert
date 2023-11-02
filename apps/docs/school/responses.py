# Imports do drf-yasg
from drf_yasg import openapi

# Imports relacionados à autenticação e respostas de autenticação
from apps.docs.authentication.me.dto_response import DTO_VALIDATION_ERRO_ME

# Imports relacionados à escola (school) e respostas relacionadas
from apps.docs.school.dto_response import (
    DTO_RESPONSE_CREATE_ACCESS_DENIED,
    DTO_RESPONSE_CREATE_BAD_REQUEST,
    DTO_RESPONSE_DELETE_ACCESS_DENIED,
    DTO_RESPONSE_DELETE_SUCESS,
    DTO_RESPONSE_DETAIL_BAD_REQUEST,
    DTO_RESPONSE_DETAIL_SCHOOL,
    DTO_RESPONSE_GET_ALL_SCHOOL,
    DTO_RESPONSE_SCHOOL_CREATED,
    DTO_RESPONSE_UPDATE_ACCESS_DENIED,
    DTO_RESPONSE_UPDATE_SUCESS,
)

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

RESPONSE_SCHOOL_CREATE = {
    201: openapi.Response(
        description='Escola criada com sucesso',
        examples={'application/json': DTO_RESPONSE_SCHOOL_CREATED},
    ),
    400: openapi.Response(
        description='Erro de validação ou responsável não existe na base de dados',
        examples={'application/json': DTO_RESPONSE_CREATE_BAD_REQUEST},
    ),
    403: openapi.Response(
        description='Acesso não autorizado',
        examples={'application/json': DTO_RESPONSE_CREATE_ACCESS_DENIED},
    ),
}

RESPONSE_SCHOOL_UPDATE = {
    202: openapi.Response(
        description="A escola foi atualizada com sucesso",
        examples={'application/json': DTO_RESPONSE_UPDATE_SUCESS},
    ),
    403: openapi.Response(
        description='Acesso não autorizado',
        examples={'application/json': DTO_RESPONSE_UPDATE_ACCESS_DENIED},
    ),
    404: openapi.Response(description='Objeto não existente na base de dados.')
}

RESPONSE_SCHOOL_DELETE = {
    202: openapi.Response(
        description="A escola foi deletada com sucesso",
        examples={'application/json': DTO_RESPONSE_DELETE_SUCESS},
    ),
    403: openapi.Response(
        description='Acesso não autorizado',
        examples={'application/json': DTO_RESPONSE_DELETE_ACCESS_DENIED},
    ),
    404: openapi.Response(description='Objeto não existente na base de dados.')
}