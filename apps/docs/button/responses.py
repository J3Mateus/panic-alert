# Imports do drf-yasg
from drf_yasg import openapi


# Imports relacionados à alert (button) e respostas relacionadas
from apps.docs.button.dto_response import (
    DTO_RESPONSE_ACCESS_DENIED,
    DTO_RESPONSE_BAD_REQUEST_NOT_FIELD,
    DTO_RESPONSE_CREATED,
    DTO_RESPONSE_DETAIL,
    DTO_RESPONSE_DETAIL_BAD_REQUEST,
    DTO_RESPONSE_GET_ALL,
    DTO_RESPONSE_UPDATE_SUCESS
)

RESPONSE_BUTTON_DETAIL = {
     200: openapi.Response(description='Informação do alerta obtida com sucesso.',examples={
          'application/json':DTO_RESPONSE_DETAIL
         }),
     400:openapi.Response(description='Erro de Validação.',examples={
          'application/json':DTO_RESPONSE_DETAIL_BAD_REQUEST
         }),
     403: openapi.Response(description='Acesso não autorizado. O usuário não tem permissão para realizar esta operação.', examples={
            'application.json':DTO_RESPONSE_ACCESS_DENIED,
     }),
     404: openapi.Response(description='Objeto não existente na base de dados.')
}

RESPONSE_BUTTON_LIST = {
     200: openapi.Response(description='Informações dos alertas obtidas com sucesso.',examples={
          'application/json':DTO_RESPONSE_GET_ALL
         }),
     403: openapi.Response(description='Acesso não autorizado. O usuário não tem permissão para realizar esta operação.', examples={
            'application/json':DTO_RESPONSE_ACCESS_DENIED,
     })
}

RESPONSE_BUTTON_CREATE = {
    201: openapi.Response(
        description='Alerta criado com sucesso',
        examples={'application/json': DTO_RESPONSE_CREATED},
    ),
    400: openapi.Response(
        description='Erro de validação: Campo obrigatório não está presente no cadastro do usuário',
        examples={'application/json': DTO_RESPONSE_BAD_REQUEST_NOT_FIELD},
    ),
    403: openapi.Response(
        description='Acesso não autorizado. O usuário não possui permissão para realizar esta operação.',
        examples={'application/json': DTO_RESPONSE_ACCESS_DENIED},
    )
}

RESPONSE_BUTTON_UPDATE = {
    202: openapi.Response(
        description="O alerta foi atualizada com sucesso",
        examples={'application/json': DTO_RESPONSE_UPDATE_SUCESS},
    ),
    403: openapi.Response(
        description='Acesso não autorizado',
        examples={'application/json': DTO_RESPONSE_ACCESS_DENIED},
    ),
    404: openapi.Response(description='Objeto não existente na base de dados.')
}