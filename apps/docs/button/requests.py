from drf_yasg import openapi

REQUEST_BUTTON_UPDATE = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'type_incident': openapi.Schema(type=openapi.FORMAT_UUID, description='Categoria de Incidente'),
        'concluded_by': openapi.Schema(type=openapi.FORMAT_UUID, description='ID do usuário responsável pela conclusão do alerta'),
        'updater_by': openapi.Schema(type=openapi.FORMAT_UUID, description='ID do usuário que realizou a atualização no alerta'),
        'responsible': openapi.Schema(type=openapi.FORMAT_UUID, description='ID do policial responsavel pela ocorrencia'),
        'description': openapi.Schema(type=openapi.TYPE_STRING, description='Descrição do alerta'),
        'problem_solving': openapi.Schema(type=openapi.TYPE_STRING, description='Descrição de como foi resolvido o alerta'),
        'status': openapi.Schema(type=openapi.TYPE_STRING, description='Statu do alerta'),
    },
)