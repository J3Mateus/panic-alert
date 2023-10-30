from drf_yasg import openapi

REQUEST_AUTHENTICATION_LOGIN_JWT = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email do usuário'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Senha do usuário'),
            },
            required=['email', 'password'],
)

REQUEST_AUTHENTICATION_LOGOUT_JWT = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='seu_token_jwt_de_atualização'),
            },
            required=['refresh'],
)