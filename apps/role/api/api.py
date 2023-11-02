# Imports do Django REST framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Imports relacionados à autenticação da API
from apps.api.mixins import ApiAuthMixin

# Imports relacionados à paginação da API
from apps.api.pagination import LimitOffsetPagination, get_paginated_response

# Imports relacionados aos papéis (roles)
from apps.role.selectors.selector import role_list
from apps.role.serializers.filter_serializer import RoleFilterSerializer
from apps.role.serializers.output_serializer import RolesSerializer


class RolesListApi(ApiAuthMixin,APIView):
    
    class Pagination(LimitOffsetPagination):
        default_limit = 20

    output_serializer = RolesSerializer
    filter_serializer = RoleFilterSerializer

    def get(self, request):
        
        filters_serializer = self.filter_serializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        roles = role_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.output_serializer,
            queryset=roles,
            request=request,
            view=self,
        )
