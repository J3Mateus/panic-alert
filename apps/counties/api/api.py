# Imports do Django REST framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.api.mixins import ApiAuthMixin

from apps.api.pagination import LimitOffsetPagination, get_paginated_response

from apps.counties.models import Counties

from apps.counties.selectors.counties import countie_get, countie_list

from apps.counties.serializers.filter_serializer import CountiesFilterSerializer
from apps.counties.serializers.output_serializer import CountieOutputSerializer

from drf_yasg.utils import swagger_auto_schema

from apps.docs.counties.response import RESPONSE_COUNTIE_BY_ID, RESPONSE_COUNTIE_LIST
class CountieListApi(ApiAuthMixin,APIView):
    
    class Pagination(LimitOffsetPagination):
        default_limit = 20

    output_serializer = CountieOutputSerializer
    filter_serializer = CountiesFilterSerializer  
    @swagger_auto_schema(
        operation_summary="Listar Counties",
        operation_description="Esta rota permite listar as counties com os filtros fornecidos. As roles serão retornadas de acordo com os filtros aplicados.",
        responses=RESPONSE_COUNTIE_LIST,
    )
    def get(self, request):
        
        filters_serializer = self.filter_serializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        counties = countie_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.output_serializer,
            queryset=counties,
            request=request,
            view=self,
        )

class CountieDetailApi(ApiAuthMixin, APIView):
    
    output_serializer = CountieOutputSerializer
    @swagger_auto_schema(
        operation_summary="Recupere detalhes de uma counties específica pelo seu ID.",
        operation_description="Use esta rota para obter informações detalhadas sobre uma countie específica com base em seu ID. Ela retorna os detalhes essenciais da counties, como nome, code e id.",
        responses=RESPONSE_COUNTIE_BY_ID,
    )     
    def get(self, request, countie_id):
        countie = countie_get(Counties, id=countie_id)
        if countie is None:
            return Response(status=404)
        data = self.output_serializer(countie).data
        return Response(status=status.HTTP_200_OK,data=data)