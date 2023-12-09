from drf_yasg import openapi

REQUEST_SCHOOL_CREATE = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Nome da escola'),
                "address": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="Endereço da escola",
                    properties={
                        'zipCode': openapi.Schema(type=openapi.TYPE_STRING, description='CEP da escola'),
                        'district': openapi.Schema(type=openapi.TYPE_STRING, description='bairro da escola'),
                        'uf': openapi.Schema(type=openapi.TYPE_STRING, description='UF da escola'),
                        'location': openapi.Schema(type=openapi.TYPE_STRING, description='localidade da escola'),
                        'publicArea': openapi.Schema(type=openapi.TYPE_STRING, description='logradouro da escola')
                    }
                ),
                'geolocation': openapi.Schema(type=openapi.TYPE_STRING, description='Geolocalização da escola'),
                'responsible': openapi.Schema(type=openapi.FORMAT_UUID, description='ID do responsável da escola'),
                'countie': openapi.Schema(type=openapi.FORMAT_UUID, description='ID do muncipio da escola'),
            },
            required=['name', 'address','geolocation','responsible','countie'],
)

REQUEST_SCHOOL_UPDATE = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "name": openapi.Schema(type=openapi.TYPE_STRING, description="O nome da escola"),
        "address": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            description="Novo endereço da escola",
            properties={
                'zipCode': openapi.Schema(type=openapi.TYPE_STRING, description='Novo CEP da escola'),
                'district': openapi.Schema(type=openapi.TYPE_STRING, description='Novo bairro da escola'),
                'uf': openapi.Schema(type=openapi.TYPE_STRING, description='Nova UF da escola'),
                'location': openapi.Schema(type=openapi.TYPE_STRING, description='Nova localidade da escola'),
                'publicArea': openapi.Schema(type=openapi.TYPE_STRING, description='Novo logradouro da escola')
            }
        ),
        "responsible": openapi.Schema(type=openapi.FORMAT_UUID, description="O ID do responsável pela escola"),
        "geolocation": openapi.Schema(type=openapi.TYPE_STRING, description="A geolocalização da escola"),      
        "is_deleted": openapi.Schema(type=openapi.TYPE_STRING, description="Estado da escola no banco de dados"),     
        'countie': openapi.Schema(type=openapi.FORMAT_UUID, description='ID do muncipio da escola'), 
    }
)