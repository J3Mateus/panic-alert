from drf_yasg import openapi

from apps.docs.authentication.me.dto_response import DTO_ME_SUCCESS, DTO_VALIDATION_ERRO_ME

RESPONSE_ME = {
     200: openapi.Response(description='Informações do usuário obtidas com sucesso.',examples={
          'application/json':DTO_ME_SUCCESS
         }),
     403: openapi.Response(description='Acesso não autorizado. O usuário não tem permissão para realizar esta operação.', examples={
            'application/json':DTO_VALIDATION_ERRO_ME,
     })
}