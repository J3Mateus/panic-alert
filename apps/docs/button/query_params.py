from drf_yasg import openapi

# Lista de Parâmetros de Consulta para a API de Escolas

QUERY_PARAM_LIST_BUTTON = [
    openapi.Parameter(
        name="id",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="ID do alerta a ser consultada.",
    ),
    openapi.Parameter(
        name="cop",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="ID da delegacia para filtrar os resultados.",
    ),
    openapi.Parameter(
        name="type_incident",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="Buscar por tipo de incidente",
    ),
    openapi.Parameter(
        name="teacher",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="ID de quem criou no alerta para filtrar os resultados.",
    ),
    openapi.Parameter(
        name="concluded_by",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="ID de quem concluiu o alerta para filtrar os resultados."
        ),
    openapi.Parameter(
        name="school",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="ID da escola de origem que foi gerado o alerta para filtrar os resultados.",
    ),
    openapi.Parameter(
        name="responsible",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="ID de quem está responsavel pelo alerta para filtrar os resultados.",
    ),
    openapi.Parameter(
        name="status",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="Status da ocorrencia para filtrar os resultados.",
    ),
     openapi.Parameter(
        name="all",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Se definido como True, a consulta buscará todas as delegacias sem paginação.",
    ),
    # Adicione outros parâmetros de consulta conforme necessário.
]
