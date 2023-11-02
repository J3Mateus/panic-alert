# Imports do Django REST framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Imports relacionados à paginação da API
from apps.api.pagination import (
    LimitOffsetPagination,
    get_paginated_response,
)

# Imports relacionados aos usuários
from apps.users.selectors import user_list
from apps.users.services.user import user_create, user_delete

# Imports relacionados à autenticação da API
from apps.api.mixins import ApiAuthMixin

# Imports de serializadores de usuários
from apps.users.serializers.output_serializer import UserOutputSerializer
from apps.users.serializers.filter_serializer import UserFilterSerializer
from apps.users.serializers.input_serializer import UserInputSerializer


class UserListApi(ApiAuthMixin,APIView):
    
    class Pagination(LimitOffsetPagination):
        default_limit = 20

    output_serializer = UserOutputSerializer
    filter_serializer = UserFilterSerializer
    
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

    input_serializer = UserInputSerializer
    output_serializer = UserOutputSerializer
    def post(self, request):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = user_create(**serializer.validated_data,created_by=request.user)
        data = self.output_serializer(user).data
        return Response(status=status.HTTP_201_CREATED,data=data)


class UserDeleteApi(ApiAuthMixin, APIView):
    
    output_serializer = UserOutputSerializer

    def delete(self, request, user_id):
        user_new = user_delete(id=user_id)
        data = self.output_serializer(user_new).data
        return Response(status=status.HTTP_202_ACCEPTED,data=data)