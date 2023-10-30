from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from drf_yasg import openapi

from apps.docs.authentication.session.dto_response import DTO_SUCCESS_SESSION,DTO_VALIDATION_ERRO_EMAIL_AND_PASSWORD_SESSION



RESPONSE_AUTHENTICATION_LOGIN_SESSION = {
            200: openapi.Response(
                description='Autenticação bem-sucedida. A sessão foi iniciada com sucesso.',
                examples={'application/json': DTO_SUCCESS_SESSION}
            ),
            400: openapi.Response(
                description='Requisição malformada, dados inválidos ou falha na autenticação.',
            ),
            401: openapi.Response(
                 description='Falha na autenticação. Verifique as credenciais fornecidas.',
                 examples={ 'application/json':DTO_VALIDATION_ERRO_EMAIL_AND_PASSWORD_SESSION,
        }),
        }