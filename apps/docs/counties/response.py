from drf_yasg import openapi

from apps.docs.counties.dto_response import DTO_RESPONSE_ACCESS_DENIED, DTO_RESPONSE_GET_ALL, DTO_RESPONSE_GET_BY_ID

RESPONSE_COUNTIE_LIST = {
    200: openapi.Response(description='Informações dos counties obtidas com sucesso.', examples={
        'application/json': DTO_RESPONSE_GET_ALL
    }),
    403: openapi.Response(description='Acesso não autorizado. O usuário não tem permissão para realizar esta operação.', examples={
        'application/json': DTO_RESPONSE_ACCESS_DENIED,
    })
}


RESPONSE_COUNTIE_BY_ID = {
    200: openapi.Response(description='Informações dos counties obtidas com sucesso.', examples={
        'application/json': DTO_RESPONSE_GET_BY_ID
    }),
    403: openapi.Response(description='Acesso não autorizado. O usuário não tem permissão para realizar esta operação.', examples={
        'application/json': DTO_RESPONSE_ACCESS_DENIED,
    })
}

