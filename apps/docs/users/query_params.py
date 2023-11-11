from drf_yasg import openapi

QUERY_PARAM_LIST_USER = [
    openapi.Parameter(
        name="id",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="ID do usuário a ser consultado.",
    ),
    openapi.Parameter(
        name="is_admin",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Filtrar os resultados por usuários que são administradores (True) ou não administradores (False).",
    ),
    openapi.Parameter(
        name="email",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="Filtrar os resultados por endereço de e-mail do usuário.",
    ),
    openapi.Parameter(
        name="is_deleted",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Se definido como True, a consulta buscará usuários excluídos. Se definido como False, buscará todos os usuários ativos. Se não for especificado, retornará ambas as opções.",
    ),
    openapi.Parameter(
        name="all",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_BOOLEAN,
        description="Se definido como True, a consulta buscará todos usuários sem paginação.",
    ),
    # Adicione outros parâmetros de consulta conforme necessário.
]


QUERY_PARAM_DELETE_USER = [
    openapi.Parameter(
        name="user_id",
        in_=openapi.IN_PATH,
        type=openapi.TYPE_STRING,
        description="O ID do usuário que deseja deletar.",
    ),
]

QUERY_PARAM_UPDATE_USER = [
    openapi.Parameter(
        name="user_id",
        in_=openapi.IN_PATH,
        type=openapi.TYPE_STRING,
        description="O ID do usuário que deseja atualizar.",
    ),
]