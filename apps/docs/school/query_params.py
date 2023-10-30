from drf_yasg import openapi

# Lista de Parâmetros de Consulta para a API de Escolas

QUERY_PARAM_LIST_SCHOOL = [
    openapi.Parameter(
        name="id",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="ID da escola a ser consultada.",
    ),
    openapi.Parameter(
        name="responsible",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="ID do responsável da escola para filtrar os resultados.",
    ),
    openapi.Parameter(
        name="created_by",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="ID do criador da escola para filtrar os resultados.",
    ),
    openapi.Parameter(
        name="deleted_by",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="ID de quem deletou a escola para filtrar os resultados.",
    ),
    openapi.Parameter(
        name="is_deleted",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Se definido como True, a consulta buscará escolas excluídas. Se definido como False, buscará todas as escolas ativas. Se não for especificado, retornará ambas as opções.",
    ),
    # Adicione outros parâmetros de consulta conforme necessário.
]


QUERY_PARAM_DETAIL_SCHOOL = [
    openapi.Parameter(
        name="school_id",
        in_=openapi.IN_PATH,
        type=openapi.TYPE_INTEGER,
        description="O ID da escola que deseja recuperar os detalhes.",
    ),
]