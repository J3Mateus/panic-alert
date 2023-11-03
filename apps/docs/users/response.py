# Imports do drf-yasg
from drf_yasg import openapi


# Imports relacionados à usuário (user) e respostas relacionadas
from apps.docs.users.dto_response import (
    DTO_RESPONSE_ACCESS_DENIED,
    DTO_RESPONSE_BAD_REQUEST_NOT_FIELD,
    DTO_RESPONSE_BAD_REQUEST_NOT_FOUND_ROLE,
    DTO_RESPONSE_BAD_REQUEST_NOT_FOUND_SCHOOL,
    DTO_RESPONSE_CONFLICT,
    DTO_RESPONSE_CREATE,
    DTO_RESPONSE_DELETE_SUCESS,
    DTO_RESPONSE_GET_ALL,
    DTO_RESPONSE_UPDATE_SUCESS
)

RESPONSE_USER_LIST = {
     200: openapi.Response(description='Informações das escolas obtidas com sucesso.',examples={
          'application/json':DTO_RESPONSE_GET_ALL
         }),
     403: openapi.Response(description='Acesso não autorizado. O usuário não tem permissão para realizar esta operação.', examples={
            'application/json':DTO_RESPONSE_ACCESS_DENIED,
     })
}

RESPONSE_USER_CREATE = {
    201: openapi.Response(
        description='Usuário criado com sucesso',
        examples={'application/json': DTO_RESPONSE_CREATE},
    ),
    400: openapi.Response(
        description='Erro de validação: Campo obrigatório não foi declarado',
        examples={'application/json': DTO_RESPONSE_BAD_REQUEST_NOT_FIELD},
    ),
    403: openapi.Response(
        description='Acesso não autorizado. O usuário não possui permissão para realizar esta operação.',
        examples={'application/json': DTO_RESPONSE_ACCESS_DENIED},
    ),
    404: openapi.Response(
        description='Recurso não encontrado. a escola não foi localizada',
        examples={'application/json': DTO_RESPONSE_BAD_REQUEST_NOT_FOUND_SCHOOL},
    ),
    404: openapi.Response(
        description='Recurso não encontrado. A função não foi localizada',
        examples={'application/json': DTO_RESPONSE_BAD_REQUEST_NOT_FOUND_ROLE},
    ),
    409: openapi.Response(
        description='Conflito. Já existe um registro com os mesmos dados',
        examples={'application/json': DTO_RESPONSE_CONFLICT},
    ),
}

RESPONSE_USER_DELETE = {
    202: openapi.Response(
        description="A escola foi deletada com sucesso",
        examples={'application/json': DTO_RESPONSE_DELETE_SUCESS},
    ),
    403: openapi.Response(
        description='Acesso não autorizado',
        examples={'application/json': DTO_RESPONSE_ACCESS_DENIED},
    ),
    400: openapi.Response(
        description='Recurso não encontrado. o usuário não foi localizada',
        examples={'application/json': DTO_RESPONSE_BAD_REQUEST_NOT_FOUND_SCHOOL},
    ),
}

RESPONSE_USER_UPDATE = {
    202: openapi.Response(
        description="A escola foi atualizada com sucesso",
        examples={'application/json': DTO_RESPONSE_UPDATE_SUCESS},
    ),
    403: openapi.Response(
        description='Acesso não autorizado',
        examples={'application/json': DTO_RESPONSE_ACCESS_DENIED},
    ),
    404: openapi.Response(description='Objeto não existente na base de dados.')
}