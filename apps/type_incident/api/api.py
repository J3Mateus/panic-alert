# Imports do Django REST framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Imports relacionados à autenticação da API
from apps.api.mixins import ApiAuthMixin

# Imports relacionados à paginação da API
from apps.api.pagination import LimitOffsetPagination, get_paginated_response


# Imports relacionados as naturezas (type_incident)
from apps.type_incident.selectors.selector import type_incident_list
from apps.type_incident.serializers.filter_serializer import TypeIncidentFilterSerializer
from apps.type_incident.serializers.output_serializer import TypeIncidentSerializer
# Imports do drf-yasg (geração de documentação Swagger)
from drf_yasg.utils import swagger_auto_schema

class TypeIncidentListApi(ApiAuthMixin,APIView):
    
    class Pagination(LimitOffsetPagination):
        default_limit = 20

    output_serializer = TypeIncidentSerializer
    filter_serializer = TypeIncidentFilterSerializer

    def get(self, request):
        
        filters_serializer = self.filter_serializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)
        all =  request.query_params.get("all")
        if all == 'true':
            # Se o parâmetro 'all' estiver presente, retorne todos os registros sem paginar
            roles = type_incident_list(filters=filters_serializer.validated_data)
            serializer = self.output_serializer(roles, many=True)
            return Response(serializer.data)
        
        roles = type_incident_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.output_serializer,
            queryset=roles,
            request=request,
            view=self,
        )
