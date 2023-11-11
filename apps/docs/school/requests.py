from drf_yasg import openapi

REQUEST_SCHOOL_CREATE = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Nome da escola'),
                'address': openapi.Schema(type=openapi.TYPE_STRING, description='Endereçõ da escola'),
                'geolocation': openapi.Schema(type=openapi.TYPE_STRING, description='Geolocalização da escola'),
                'responsible': openapi.Schema(type=openapi.TYPE_STRING, description='ID do responsável da escola'),
                'countie': openapi.Schema(type=openapi.TYPE_STRING, description='ID do muncipio da escola'),
            },
            required=['name', 'address','geolocation','responsible','countie'],
)

REQUEST_SCHOOL_UPDATE = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "name": openapi.Schema(type=openapi.TYPE_STRING, description="O nome da escola"),
        "address": openapi.Schema(type=openapi.TYPE_STRING, description="O endereço da escola"),
        "responsible": openapi.Schema(type=openapi.TYPE_STRING, description="O nome do responsável pela escola"),
        "geolocation": openapi.Schema(type=openapi.TYPE_STRING, description="A geolocalização da escola"),      
        "is_deleted": openapi.Schema(type=openapi.TYPE_STRING, description="Estado da escola no banco de dados"),     
        'countie': openapi.Schema(type=openapi.TYPE_STRING, description='ID do muncipio da escola'), 
    }
)