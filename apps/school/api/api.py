# Imports do Django REST framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Imports do drf-yasg (geração de documentação Swagger)
from drf_yasg.utils import swagger_auto_schema

# Imports relacionados à autenticação da API
from apps.api.mixins import ApiAuthMixin

# Imports de parâmetros de consulta da API
from apps.docs.school.query_params import (
    QUERY_PARAM_DELETE_SCHOOL,
    QUERY_PARAM_DETAIL_SCHOOL,
    QUERY_PARAM_LIST_SCHOOL,
)

# Imports de solicitações da API
from apps.docs.school.requests import (
    REQUEST_SCHOOL_CREATE,
    REQUEST_SCHOOL_UPDATE,
)

# Imports de respostas da API
from apps.docs.school.responses import (
    RESPONSE_SCHOOL_CREATE,
    RESPONSE_SCHOOL_DELETE,
    RESPONSE_SCHOOL_DETAIL,
    RESPONSE_SCHOOL_LIST,
    RESPONSE_SCHOOL_UPDATE,
)

# Imports relacionados à serialização de dados
from apps.school.serializers.filter_serializer import SchoolFilterSerializer
from apps.school.serializers.input_serializer import SchoolCreateInputSerializer, SchoolUpdateInputSerializer
from apps.school.serializers.output_serializer import SchoolOutputSerializer

# Imports de modelos e seletores
from apps.school.models import School
from apps.school.selectors.selector import school_get, school_list

# Imports de serviços e paginação
from apps.school.services.school import school_create, school_delete, school_update
from apps.api.pagination import (
    LimitOffsetPagination,
    get_paginated_response,
)

from panicButton.settings import BASE_SOCKET_URL

import socketio

class SchoolListApi(ApiAuthMixin,APIView):
    
    class Pagination(LimitOffsetPagination):
        default_limit = 20

    output_serializer = SchoolOutputSerializer
    filter_serializer = SchoolFilterSerializer
    @swagger_auto_schema(
        operation_summary="Recupere uma lista paginada de escolas.",
        manual_parameters=QUERY_PARAM_LIST_SCHOOL,
        operation_description="Esta rota permite a recuperação de uma lista paginada de escolas. Ela suporta filtragem com base em parâmetros específicos e fornece resultados paginados, tornando mais fácil a navegação por um grande número de escolas",
        responses=RESPONSE_SCHOOL_LIST
        )    
    def get(self, request):
        
        filters_serializer = self.filter_serializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)
        all =  request.query_params.get("all")
        if all == 'true':
            # Se o parâmetro 'all' estiver presente, retorne todos os registros sem paginar
            schools = school_list(filters=filters_serializer.validated_data)
            serializer = self.output_serializer(schools, many=True)
            return Response(serializer.data)
        
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
        operation_summary="Recupere detalhes de uma escola específica pelo seu ID.",
        operation_description="Use esta rota para obter informações detalhadas sobre uma escola específica com base em seu ID. Ela retorna os detalhes essenciais da escola, como nome, localização e outras informações relevantes.",
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

    input_serializer = SchoolCreateInputSerializer
    output_serializer = SchoolOutputSerializer
    
    @swagger_auto_schema(
        operation_summary="Crie uma escola.",
        operation_description="Esta rota é usada para criar uma nova escola no sistema. Os dados da escola são fornecidos no corpo da solicitação, e a escola é criada com base nessas informações. O endpoint retorna os detalhes da escola recém-criada.",
        request_body=REQUEST_SCHOOL_CREATE,
        responses=RESPONSE_SCHOOL_CREATE,
    )     
    def post(self, request):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        school = school_create(**serializer.validated_data,user=request.user)
        
        data = self.output_serializer(school).data
        try:
            with socketio.SimpleClient() as sio:
                sio = socketio.SimpleClient()
                sio.connect(BASE_SOCKET_URL)
                sio.emit("create_room", data.get("id"))
        except ConnectionError as e:
            pass
        
        return Response(status=status.HTTP_201_CREATED,data=data)

class SchoolUpdateApi(ApiAuthMixin, APIView):
    
    input_serializer = SchoolUpdateInputSerializer
    output_serializer = SchoolOutputSerializer
    
    @swagger_auto_schema(
        operation_summary="Atualize os detalhes de uma escola existente.",
        operation_description="Utilize esta rota para atualizar os detalhes de uma escola existente. Os dados de atualização são fornecidos no corpo da solicitação, e a escola é atualizada com base nesses dados. A rota retorna os detalhes da escola atualizada.",
        request_body=REQUEST_SCHOOL_UPDATE,
        responses=RESPONSE_SCHOOL_UPDATE,
    )    
    
    def patch(self, request, school_id):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        school = school_get(school=School, id=school_id)
        if school is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        school_new = school_update(school=school,data=serializer.validated_data)
        data = self.output_serializer(school_new).data
        return Response(status=status.HTTP_202_ACCEPTED,data=data)

class SchoolDeleteApi(ApiAuthMixin, APIView):
    
    output_serializer = SchoolOutputSerializer
    @swagger_auto_schema(
        operation_summary="Exclua uma escola.",
        operation_description="Esta rota permite a exclusão de uma escola com base em seu ID. Após a exclusão bem-sucedida, a escola não estará mais disponível no sistema. A rota retorna os detalhes da escola excluída.",
        manual_parameters=QUERY_PARAM_DELETE_SCHOOL,
        responses=RESPONSE_SCHOOL_DELETE,
    )
    
    def delete(self, request, school_id):
        school_new = school_delete(id=school_id)
        if school_new is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = self.output_serializer(school_new).data
        return Response(status=status.HTTP_202_ACCEPTED,data=data)