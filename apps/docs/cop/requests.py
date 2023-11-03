from drf_yasg import openapi

REQUEST_COP_CREATE = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Nome da delegacia'),
                'address': openapi.Schema(type=openapi.TYPE_STRING, description='Endereço da delegacia'),
                'geolocation': openapi.Schema(type=openapi.TYPE_STRING, description='Geolocalização da delegacia'),
                'responsible': openapi.Schema(type=openapi.TYPE_STRING, description='ID do responsável da delegacia'),
            },
            required=['name', 'address','geolocation','responsible'],
)

REQUEST_COP_UPDATE = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "name": openapi.Schema(type=openapi.TYPE_STRING, description="O nome da delegacia"),
        "address": openapi.Schema(type=openapi.TYPE_STRING, description="O endereço da delegacia"),
        "responsible": openapi.Schema(type=openapi.TYPE_STRING, description="O nome do responsável pela delegacia"),
        "geolocation": openapi.Schema(type=openapi.TYPE_STRING, description="A geolocalização da delegacia"),      
        "is_deleted": openapi.Schema(type=openapi.TYPE_STRING, description="Estado da delegacia no banco de dados"),      
    }
)