# Imports do Django REST framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Imports relacionados à paginação da API
from apps.api.pagination import (
    LimitOffsetPagination,
    get_paginated_response,
)

# Imports do drf-yasg (geração de documentação Swagger)
from drf_yasg.utils import swagger_auto_schema

# Imports relacionados à documentação da API de usuários
from apps.docs.users.query_params import QUERY_PARAM_DELETE_USER, QUERY_PARAM_LIST_USER, QUERY_PARAM_UPDATE_USER
from apps.docs.users.requests import REQUEST_USER_CREATE, REQUEST_USER_UPDATE
from apps.docs.users.response import RESPONSE_USER_CREATE, RESPONSE_USER_DELETE, RESPONSE_USER_LIST, RESPONSE_USER_UPDATE

# Imports relacionados aos usuários
from apps.users.selectors import user_list
from apps.users.selectors.user import get_user_by_email, user_get
from apps.users.services.user import user_create, user_delete, user_update

# Imports relacionados à autenticação da API
from apps.api.mixins import ApiAuthMixin

# Imports de serializadores de usuários
from apps.users.serializers.output_serializer import UserOutputSerializer
from apps.users.serializers.filter_serializer import UserFilterSerializer
from apps.users.serializers.input_serializer import UserCreateInputSerializer, UserUpdateInputSerializer



class UserListApi(ApiAuthMixin,APIView):
    
    class Pagination(LimitOffsetPagination):
        default_limit = 20

    output_serializer = UserOutputSerializer
    filter_serializer = UserFilterSerializer
    
    @swagger_auto_schema(
        operation_summary="Lista de Usuários",
        operation_description="Esta rota permite a consulta de usuários com base em filtros específicos. Você pode filtrar por ID do usuário, se é administrador, endereço de e-mail e status de exclusão.",
        manual_parameters=QUERY_PARAM_LIST_USER,
        responses=RESPONSE_USER_LIST,
    )
        
    def get(self, request):
        # Make sure the filters are valid, if passed
        filters_serializer = self.filter_serializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        users = user_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.output_serializer,
            queryset=users,
            request=request,
            view=self,
        )

class UserCreateApi(ApiAuthMixin, APIView):

    input_serializer = UserCreateInputSerializer
    output_serializer = UserOutputSerializer
    @swagger_auto_schema(
        operation_summary="Criar um Usuário",
        operation_description="Esta rota permite a criação de um novo usuário com os dados fornecidos. O usuário não deve existir previamente no banco de dados. Se o email fornecido já estiver em uso, a criação falhará.",
        request_body=REQUEST_USER_CREATE,
        responses=RESPONSE_USER_CREATE,
    )
    def post(self, request):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        verify_user = get_user_by_email(email=email)
        
        if verify_user :
            return Response(status=status.HTTP_409_CONFLICT,data={
                "message":{"detail": "A chave única já existe no banco de dados."},
                "code": "Conflict",
                "messages": [
                    {
                        "field": "email",
                        "message": "O email já está sendo usado por um usuario"
                    }
                ],
                "extra": {}
                })
        
        user = user_create(**serializer.validated_data,created_by=request.user)
        data = self.output_serializer(user).data
        return Response(status=status.HTTP_201_CREATED,data=data)


class UserDeleteApi(ApiAuthMixin, APIView):
    
    output_serializer = UserOutputSerializer
    
    @swagger_auto_schema(
        operation_summary="Excluir um Usuário",
        operation_description="Esta rota permite a exclusão de um usuário com base em seu ID. Após a exclusão bem-sucedida, o usuário não estará mais disponível no sistema. A rota retorna os detalhes do usuário excluído.",
        manual_parameters=QUERY_PARAM_DELETE_USER,
        responses=RESPONSE_USER_DELETE,
    )
    def delete(self, request, user_id):
        user_new = user_delete(id=user_id)
        data = self.output_serializer(user_new).data
        return Response(status=status.HTTP_202_ACCEPTED,data=data)

class UserUpdateApi(ApiAuthMixin, APIView):
    
    input_serializer = UserUpdateInputSerializer
    output_serializer = UserOutputSerializer
    @swagger_auto_schema(
        operation_summary="Atualizar um Usuário",
        manual_parameters=QUERY_PARAM_UPDATE_USER,
        operation_description="Esta rota permite a atualização de um usuário com base em seu ID. Você pode fornecer dados para atualizar o usuário, como nome, email, etc. A rota retorna os detalhes do usuário após a atualização.",
        responses=RESPONSE_USER_UPDATE,
        request_body=REQUEST_USER_UPDATE,
    )
    
    def patch(self, request, user_id):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = user_get(pk=user_id)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        new_user = user_update(user=user,data=serializer.validated_data)
        data = self.output_serializer(new_user).data
        return Response(status=status.HTTP_202_ACCEPTED,data=data)
