# Imports do Django REST framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Imports do drf-yasg (geração de documentação Swagger)
from drf_yasg.utils import swagger_auto_schema

# Imports relacionados à autenticação da API
from apps.api.mixins import ApiAuthMixin

# Imports de parâmetros de consulta da API
from apps.docs.cop.query_params import (
    QUERY_PARAM_LIST_COP
)

# Imports de solicitações da API
from apps.docs.cop.requests import (
    REQUEST_COP_CREATE,
    REQUEST_COP_UPDATE,
)

# Imports de respostas da API
from apps.docs.cop.responses import (
    RESPONSE_COP_CREATE,
    RESPONSE_COP_DELETE,
    RESPONSE_COP_DETAIL,
    RESPONSE_COP_LIST,
    RESPONSE_COP_UPDATE,
)

# Imports relacionados à serialização de dados
from apps.cop.serializers.filter_serializer import COPFilterSerializer
from apps.cop.serializers.input_serializer import COPCreateInputSerializer, COPUpdateInputSerializer
from apps.cop.serializers.output_serializer import COPOutputSerializer

# Imports de modelos e seletores
from apps.cop.models import COP
from apps.cop.selectors.selector import cop_get, cop_list

# Imports de serviços e paginação
from apps.cop.services.cop import cop_create, cop_delete, cop_update
from apps.api.pagination import (
    LimitOffsetPagination,
    get_paginated_response,
)


class CopListApi(ApiAuthMixin,APIView):
    
    class Pagination(LimitOffsetPagination):
        default_limit = 20

    output_serializer = COPOutputSerializer
    filter_serializer = COPFilterSerializer
    @swagger_auto_schema(
        operation_summary="Recupere uma lista paginada de Delegacias.",
        manual_parameters=QUERY_PARAM_LIST_COP,
        operation_description="Esta rota permite a recuperação de uma lista paginada de Delegacias. Ela suporta filtragem com base em parâmetros específicos e fornece resultados paginados, tornando mais fácil a navegação por um grande número de Delegacias.",
        responses=RESPONSE_COP_LIST
        )  
    def get(self, request):
        
        filters_serializer = self.filter_serializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        cops = cop_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.output_serializer,
            queryset=cops,
            request=request,
            view=self,
        )

class CopDetailApi(ApiAuthMixin, APIView):
    
    output_serializer = COPOutputSerializer
    @swagger_auto_schema(
        operation_summary="Recupere detalhes de uma Delegacia específica pelo seu ID.",
        operation_description="Use esta rota para obter informações detalhadas sobre uma Delegacia específica com base em seu ID. Ela retorna os detalhes essenciais da Delegacia, como nome, localização e outras informações relevantes.",
        responses=RESPONSE_COP_DETAIL,
    )      
    def get(self, request, cop_id):
        cop = cop_get(COP, id=cop_id)
        if cop is None:
            return Response(status=404)
        data = self.output_serializer(cop).data
        return Response(status=status.HTTP_200_OK,data=data)

class CopCreateApi(ApiAuthMixin, APIView):

    input_serializer = COPCreateInputSerializer
    output_serializer = COPOutputSerializer
    
    @swagger_auto_schema(
        operation_summary="Crie uma Delegacia.",
        operation_description="Esta rota é usada para criar uma nova Delegacia no sistema. Os dados da Delegacia são fornecidos no corpo da solicitação, e a Delegacia é criada com base nessas informações. O endpoint retorna os detalhes da Delegacia recém-criada.",
        request_body=REQUEST_COP_CREATE,
        responses=RESPONSE_COP_CREATE,
    )   
    def post(self, request):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cop = cop_create(**serializer.validated_data,user=request.user)
        data = self.output_serializer(cop).data
        return Response(status=status.HTTP_201_CREATED,data=data)

class CopUpdateApi(ApiAuthMixin, APIView):
    
    input_serializer = COPUpdateInputSerializer
    output_serializer = COPOutputSerializer
    
    @swagger_auto_schema(
        operation_summary="Atualize os detalhes de uma Delegacia existente.",
        operation_description="Utilize esta rota para atualizar os detalhes de uma Delegacia existente. Os dados de atualização são fornecidos no corpo da solicitação, e a Delegacia é atualizada com base nesses dados. A rota retorna os detalhes da Delegacia atualizada.",
        request_body=REQUEST_COP_UPDATE,
        responses=RESPONSE_COP_UPDATE,
    )     
    
    def patch(self, request, cop_id):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cop = cop_get(cop=COP, id=cop_id)
        if cop is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        new_cop = cop_update(cop=cop,data=serializer.validated_data)
        data = self.output_serializer(new_cop).data
        return Response(status=status.HTTP_202_ACCEPTED,data=data)

class CopDeleteApi(ApiAuthMixin, APIView):
    
    output_serializer = COPOutputSerializer
    @swagger_auto_schema(
        operation_summary="Exclua uma Delegacia.",
        operation_description="Esta rota permite a exclusão de uma Delegacia com base em seu ID. Após a exclusão bem-sucedida, a Delegacia não estará mais disponível no sistema. A rota retorna os detalhes da Delegacia excluída.",
        responses=RESPONSE_COP_DELETE,
    )
    
    def delete(self, request, cop_id):
        new_cop = cop_delete(id=cop_id)
        if new_cop is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = self.output_serializer(new_cop).data
        return Response(status=status.HTTP_202_ACCEPTED,data=data)