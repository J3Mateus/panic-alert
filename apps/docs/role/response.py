from drf_yasg import openapi

from apps.docs.role.dto_response import DTO_RESPONSE_ACCESS_DENIED, DTO_RESPONSE_GET_ALL

RESPONSE_ROLE_LIST = {
    200: openapi.Response(description='Informações das roles obtidas com sucesso.', examples={
        'application/json': DTO_RESPONSE_GET_ALL
    }),
    403: openapi.Response(description='Acesso não autorizado. O usuário não tem permissão para realizar esta operação.', examples={
        'application/json': DTO_RESPONSE_ACCESS_DENIED,
    })
}
