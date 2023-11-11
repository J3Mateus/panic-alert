from drf_yasg import openapi

# Lista de Parâmetros de Consulta para a API de Escolas

QUERY_PARAM_LIST_COP = [
    openapi.Parameter(
        name="id",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="ID da delegacia a ser consultada.",
    ),
    openapi.Parameter(
        name="responsible",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="ID do responsável da delegacia para filtrar os resultados.",
    ),
    openapi.Parameter(
        name="created_by",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="ID do criador da delegacia para filtrar os resultados.",
    ),
    openapi.Parameter(
        name="deleted_by",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="ID de quem deletou a delegacia para filtrar os resultados.",
    ),
    openapi.Parameter(
        name="is_deleted",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Se definido como True, a consulta buscará delegacias excluídas. Se definido como False, buscará todas as delegacias ativas. Se não for especificado, retornará ambas as opções.",
    ),
     openapi.Parameter(
        name="all",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Se definido como True, a consulta buscará todas as delegacias sem paginação.",
    ),
    # Adicione outros parâmetros de consulta conforme necessário.
]
