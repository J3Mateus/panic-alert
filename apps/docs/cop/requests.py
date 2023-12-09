from drf_yasg import openapi

REQUEST_COP_CREATE = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Nome da delegacia'),
        'address': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            description='Informações de endereço da delegacia',
            properties={
                'zipCode': openapi.Schema(type=openapi.TYPE_STRING, description='CEP da delegacia'),
                'district': openapi.Schema(type=openapi.TYPE_STRING, description='Bairro da delegacia'),
                'uf': openapi.Schema(type=openapi.TYPE_STRING, description='UF da delegacia'),
                'location': openapi.Schema(type=openapi.TYPE_STRING, description='Localidade da delegacia'),
                'publicArea': openapi.Schema(type=openapi.TYPE_STRING, description='Logradouro da delegacia')
            }
        ),
        'geolocation': openapi.Schema(type=openapi.TYPE_STRING, description='Geolocalização da delegacia'),
        'responsible': openapi.Schema(type=openapi.FORMAT_UUID, description='ID do responsável da delegacia'),
        'countie': openapi.Schema(type=openapi.FORMAT_UUID, description='ID do município da delegacia'),
    },
    required=['name', 'address', 'geolocation', 'responsible', 'countie'],
)

REQUEST_COP_UPDATE = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "name": openapi.Schema(type=openapi.TYPE_STRING, description="Novo nome da delegacia"),
        "address": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            description="Novo endereço da delegacia",
            properties={
                'zipCode': openapi.Schema(type=openapi.TYPE_STRING, description='Novo CEP da delegacia'),
                'district': openapi.Schema(type=openapi.TYPE_STRING, description='Novo bairro da delegacia'),
                'uf': openapi.Schema(type=openapi.TYPE_STRING, description='Nova UF da delegacia'),
                'location': openapi.Schema(type=openapi.TYPE_STRING, description='Nova localidade da delegacia'),
                'publicArea': openapi.Schema(type=openapi.TYPE_STRING, description='Novo logradouro da delegacia')
            }
        ),
        "responsible": openapi.Schema(type=openapi.TYPE_STRING, description="Novo nome do responsável pela delegacia"),
        "geolocation": openapi.Schema(type=openapi.TYPE_STRING, description="Nova geolocalização da delegacia"),      
        "is_deleted": openapi.Schema(type=openapi.TYPE_BOOLEAN, description="Novo estado da delegacia no banco de dados"),      
        'countie': openapi.Schema(type=openapi.FORMAT_UUID, description='Novo ID do município da delegacia'), 
    }
)