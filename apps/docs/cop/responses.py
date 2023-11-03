# Imports do drf-yasg
from drf_yasg import openapi

# Imports relacionados à autenticação e respostas de autenticação
from apps.docs.authentication.me.dto_response import DTO_VALIDATION_ERRO_ME

# Imports relacionados à Delegacia (COP) e respostas relacionadas
from apps.docs.cop.dto_response import (
    DTO_RESPONSE_CREATE_BAD_REQUEST,
    DTO_RESPONSE_DELETE_SUCESS,
    DTO_RESPONSE_DETAIL_BAD_REQUEST,
    DTO_RESPONSE_DETAIL_COP,
    DTO_RESPONSE_GET_ALL_COP,
    DTO_RESPONSE_COP_CREATED,
    DTO_RESPONSE_DENIED,
    DTO_RESPONSE_UPDATE_SUCESS
)

RESPONSE_COP_LIST = {
     200: openapi.Response(description='Informações das Delegacias obtidas com sucesso.',examples={
          'application/json':DTO_RESPONSE_GET_ALL_COP
         }),
     403: openapi.Response(description='Acesso não autorizado. O usuário não tem permissão para realizar esta operação.', examples={
            'application/json':DTO_VALIDATION_ERRO_ME,
     })
}

RESPONSE_COP_DETAIL = {
     200: openapi.Response(description='Informação da Delegacia obtida com sucesso.',examples={
          'application/json':DTO_RESPONSE_DETAIL_COP
         }),
     400:openapi.Response(description='Erro de Validação.',examples={
          'application/json':DTO_RESPONSE_DETAIL_BAD_REQUEST
         }),
     403: openapi.Response(description='Acesso não autorizado. O usuário não tem permissão para realizar esta operação.', examples={
            'application.json':DTO_VALIDATION_ERRO_ME,
     }),
     404: openapi.Response(description='Objeto não existente na base de dados.')
}

RESPONSE_COP_CREATE = {
    201: openapi.Response(
        description='Delegacia criada com sucesso',
        examples={'application/json': DTO_RESPONSE_COP_CREATED},
    ),
    400: openapi.Response(
        description='Erro de validação ou responsável não existe na base de dados',
        examples={'application/json': DTO_RESPONSE_CREATE_BAD_REQUEST},
    ),
    403: openapi.Response(
        description='Acesso não autorizado',
        examples={'application.json': DTO_RESPONSE_DENIED},
    ),
}

RESPONSE_COP_UPDATE = {
    202: openapi.Response(
        description="A Delegacia foi atualizada com sucesso",
        examples={'application.json': DTO_RESPONSE_UPDATE_SUCESS},
    ),
    403: openapi.Response(
        description='Acesso não autorizado',
        examples={'application.json': DTO_RESPONSE_DENIED},
    ),
    404: openapi.Response(description='Objeto não existente na base de dados.')
}

RESPONSE_COP_DELETE = {
    202: openapi.Response(
        description="A Delegacia foi deletada com sucesso",
        examples={'application.json': DTO_RESPONSE_DELETE_SUCESS},
    ),
    403: openapi.Response(
        description='Acesso não autorizado',
        examples={'application.json': DTO_RESPONSE_DENIED},
    ),
    404: openapi.Response(description='Objeto não existente na base de dados.')
}
