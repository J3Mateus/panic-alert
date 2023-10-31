from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema
from apps.api.mixins import ApiAuthMixin
from apps.docs.school.query_params import QUERY_PARAM_DETAIL_SCHOOL, QUERY_PARAM_LIST_SCHOOL
from apps.docs.school.responses import RESPONSE_SCHOOL_DETAIL, RESPONSE_SCHOOL_LIST
from apps.school.serializers.filter_serializer import SchoolFilterSerializer
from apps.school.models import School
from apps.school.selectors.selector import school_get, school_list
from apps.school.serializers.input_serializer import SchoolInputSerializer
from apps.school.serializers.output_serializer import SchoolOutputSerializer
from apps.school.services.school import school_create, school_delete, school_update
from apps.api.pagination import (
    LimitOffsetPagination,
    get_paginated_response,
)

class SchoolListApi(ApiAuthMixin,APIView):
    
    class Pagination(LimitOffsetPagination):
        default_limit = 20

    output_serializer = SchoolOutputSerializer
    filter_serializer = SchoolFilterSerializer
    @swagger_auto_schema(
        operation_summary="Listar Escolas",
        manual_parameters=QUERY_PARAM_LIST_SCHOOL,
        operation_description="Recupere uma lista paginada de escolas.",
        responses=RESPONSE_SCHOOL_LIST
        )    
    def get(self, request):
        
        filters_serializer = self.filter_serializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        schools = school_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.output_serializer,
            queryset=schools,
            request=request,
            view=self,
        )


class SchoolDetailApi(ApiAuthMixin, APIView):
    
    output_serializer = SchoolOutputSerializer
    @swagger_auto_schema(
        operation_summary="Detalhes da Escola",
        operation_description="Recupere detalhes de uma escola específica pelo seu ID.",
        manual_parameters=QUERY_PARAM_DETAIL_SCHOOL,
        responses=RESPONSE_SCHOOL_DETAIL,
    )            
    def get(self, request, school_id):
        school = school_get(School, id=school_id)
        if school is None:
            return Response(status=404)
        data = self.output_serializer(school).data
        return Response(status=status.HTTP_200_OK,data=data)

class SchoolCreateApi(ApiAuthMixin, APIView):

    input_serializer = SchoolInputSerializer
    output_serializer = SchoolOutputSerializer
    def post(self, request):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        school = school_create(**serializer.validated_data,user=request.user)
        data = self.output_serializer(school).data
        return Response(status=status.HTTP_201_CREATED,data=data)

class SchoolUpdateApi(ApiAuthMixin, APIView):
    
    input_serializer = SchoolInputSerializer
    output_serializer = SchoolOutputSerializer

    def patch(self, request, school_id):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        school = school_get(school=School, id=school_id)
        school_new = school_update(school=school,data=serializer.validated_data)
        data = self.output_serializer(school_new).data
        return Response(status=status.HTTP_202_ACCEPTED,data=data)

class SchoolDeleteApi(ApiAuthMixin, APIView):
    
    output_serializer = SchoolOutputSerializer

    def delete(self, request, school_id):
        school_new = school_delete(id=school_id)
        data = self.output_serializer(school_new).data
        return Response(status=status.HTTP_202_ACCEPTED,data=data)