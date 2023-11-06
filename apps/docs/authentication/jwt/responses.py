from drf_yasg import openapi

from apps.docs.authentication.jwt.dto_response import (
     DTO_SUCCESS_JWT,
     DTO_VALIDATION_ERRO_EMAIL_AND_PASSWORD_JWT,
     DTO_VALIDATION_ERRO_LOGOUT_JWT,
     DTO_VALIDATION_INCORRECT_EMAIL_AND_PASSWORD_JWT,
     DTO_VALIDATION_USER_DELETED_JWT
)



RESPONSE_AUTHENTICATION_LOGIN_JWT = {
     200: openapi.Response(description='Autenticação bem-sucedida. Retorna um token JWT válido.',examples={
          'application/json':DTO_SUCCESS_JWT
         }),
     401: openapi.Response(description='Falha na autenticação. Verifique as credenciais fornecidas.',examples={
          'application/json':DTO_VALIDATION_ERRO_EMAIL_AND_PASSWORD_JWT,
        }),
     400: openapi.Response(description='Falha na autenticação. usuário foi desativado.', examples={
            'application/json':DTO_VALIDATION_USER_DELETED_JWT,
        }),
     400: openapi.Response(description='Requisição malformada ou dados ausentes.', examples={
            'application/json':DTO_VALIDATION_INCORRECT_EMAIL_AND_PASSWORD_JWT,
        })
}

RESPONSE_AUTHENTICATION_LOGOUT_JWT = {
     200: openapi.Response(description='Sessão encerrada com sucesso e tokens JWT revogados'),
     403: openapi.Response(description='Acesso não autorizado. O usuário não tem permissão para realizar esta operação.', examples={
            'application/json':DTO_VALIDATION_ERRO_LOGOUT_JWT,
     })
}