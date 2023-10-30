from drf_yasg import openapi

REQUEST_AUTHENTICATION_LOGIN_SESSION = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email do usuário'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Senha do usuário'),
            },
            required=['email', 'password'],
)