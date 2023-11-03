from drf_yasg import openapi

REQUEST_USER_CREATE = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Endereço de email do usuário'),
        'phone': openapi.Schema(type=openapi.TYPE_STRING, description='Número de telefone do usuário'),
        'whatsapp': openapi.Schema(type=openapi.TYPE_STRING, description='Número do WhatsApp do usuário'),
        'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='Primeiro nome do usuário'),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Sobrenome do usuário'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='Senha do usuário'),
        'roles': openapi.Schema(type=openapi.TYPE_ARRAY,items=openapi.Items(type=openapi.TYPE_STRING), description='Funções do usuário'),
        'cops':openapi.Schema(type=openapi.TYPE_ARRAY,items=openapi.Items(type=openapi.TYPE_STRING), description='ID das delegacias associadas ao usuário'),
        'schools':openapi.Schema(type=openapi.TYPE_ARRAY,items=openapi.Items(type=openapi.TYPE_STRING),description='ID das escolas associadas ao usuário'),
    },
    required=['email', 'phone', 'whatsapp', 'first_name', 'last_name', 'password', 'roles'],
)


REQUEST_USER_UPDATE = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Endereço de email do usuário'),
        'phone': openapi.Schema(type=openapi.TYPE_STRING, description='Número de telefone do usuário'),
        'whatsapp': openapi.Schema(type=openapi.TYPE_STRING, description='Número do WhatsApp do usuário'),
        'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='Primeiro nome do usuário'),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Sobrenome do usuário'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='Senha do usuário'),
        'role': openapi.Schema(type=openapi.TYPE_ARRAY,items=openapi.Items(type=openapi.TYPE_STRING), description='Funções do usuário'),
        'cop': openapi.Schema(type=openapi.TYPE_ARRAY,items=openapi.Items(type=openapi.TYPE_STRING), description='ID das delegacias associada ao usuário'), 
        'school': openapi.Schema(type=openapi.TYPE_STRING, description='ID das escolas associadas ao usuário'),
    },
)