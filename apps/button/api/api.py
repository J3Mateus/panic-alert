from rest_framework.views import APIView
from rest_framework.response import Response
import socketio
from apps.api.pagination import LimitOffsetPagination, get_paginated_response
from apps.button.selectors.selector import button_get, button_list, button_list_status
from rest_framework import status
from apps.button.serializers.filter_serializer import ButtonFilterSerializer
from apps.button.serializers.input_serializer import ButtonUpdateInputSerializer

from apps.button.serializers.output_serializer import ButtonOutputSerializer
from apps.button.service.button import button_create, button_update

from apps.api.mixins import ApiAuthMixin

from apps.button.models import Button
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.docs.button.query_params import QUERY_PARAM_LIST_BUTTON
from apps.docs.button.requests import REQUEST_BUTTON_UPDATE
from apps.docs.button.responses import RESPONSE_BUTTON_CREATE, RESPONSE_BUTTON_DETAIL, RESPONSE_BUTTON_LIST, RESPONSE_BUTTON_UPDATE
from panicButton.settings import BASE_SOCKET_URL
class ButtonListApi(ApiAuthMixin,APIView):
    
    class Pagination(LimitOffsetPagination):
        default_limit = 20

    output_serializer = ButtonOutputSerializer
    filter_serializer = ButtonFilterSerializer
    @swagger_auto_schema(
        manual_parameters=QUERY_PARAM_LIST_BUTTON,
        responses=RESPONSE_BUTTON_LIST,
        operation_summary="Listar Alerta",
        operation_description="Retorna uma lista de alerta com opção de filtragem.",
    )        
    def get(self, request):
        """
        Listar Alertas com opção de filtragem.
        """        
        filters_serializer = self.filter_serializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)
        all =  request.query_params.get("all")
        if all == 'true':
            # Se o parâmetro 'all' estiver presente, retorne todos os registros sem paginar
            schools = button_list(filters=filters_serializer.validated_data)
            serializer = self.output_serializer(schools, many=True)
            return Response(serializer.data)
        
        schools = button_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.output_serializer,
            queryset=schools,
            request=request,
            view=self,
        )
        
class ButtonDetailApi(ApiAuthMixin,APIView):
    
    output_serializer = ButtonOutputSerializer
    @swagger_auto_schema(
        manual_parameters=None,
        responses=RESPONSE_BUTTON_DETAIL,
        operation_summary="Detalhes do Alerta",
        operation_description="Obtém detalhes de um alerta.",
    )     
    def get(self,request,button_id):
       button: Button =  button_get(id=button_id)
       
       if button is None:
           return Response(status=status.HTTP_404_NOT_FOUND)
       
       data = self.output_serializer(button).data
       
       return Response(status=status.HTTP_200_OK,data=data)

class ButtonListStatusApi(ApiAuthMixin,APIView):
    
    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="Lista de Status",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'value': openapi.Schema(type=openapi.TYPE_STRING),
                            'label': openapi.Schema(type=openapi.TYPE_STRING)
                        }
                    )
                ),
                examples={
                    "application/json": [
                        {
                            "value": "ajuda_caminho",
                            "label": "Ajuda a Caminho"
                        },
                        {
                            "value": "ocorrencia_resolvida",
                            "label": "Ocorrência Resolvida"
                        },
                        {
                            "value": "ocorrencia_iniciada",
                            "label": "Ocorrência iniciada"
                        }
                    ]
                }
            )
        },
        operation_summary="Lista de Status",
        operation_description="Retorna uma lista dos status disponíveis."
    )
    def get(self,request):
        list_status_button = button_list_status()
        return Response(status=status.HTTP_200_OK,data=list_status_button)
    
class ButtonCreateApi(ApiAuthMixin,APIView):
    
    output_serializer = ButtonOutputSerializer
    @swagger_auto_schema(
        request_body=None,
        responses=RESPONSE_BUTTON_CREATE,
        operation_summary="Criar um novo Alerta",
        operation_description="Cria uma nova instância de Alerta associada ao usuário atual.",
    )    
    def post(self,request):
        """
        Criar um novo Botão associado ao usuário atual.
        """        
        button = button_create(user=request.user)
        data = self.output_serializer(button).data
        
        with socketio.SimpleClient() as sio:
            sio = socketio.SimpleClient()
            sio.connect(BASE_SOCKET_URL)
            sio.emit("alert",data)
            
        return Response(status=status.HTTP_201_CREATED,data=data)

class ButtonUpdateApi(ApiAuthMixin, APIView):
    
    input_serializer = ButtonUpdateInputSerializer
    output_serializer = ButtonOutputSerializer
    @swagger_auto_schema(
        request_body=REQUEST_BUTTON_UPDATE,
        responses=RESPONSE_BUTTON_UPDATE,
        operation_summary="Atualizar um Alerta Existente",
        operation_description="Atualiza uma instância existente de Alerta associada ao usuário atual."
    )  
    def patch(self, request, button_id):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        button = button_get(id=button_id)
        if button is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        school_new = button_update(button=button,data=serializer.validated_data)
        data = self.output_serializer(school_new).data
        return Response(status=status.HTTP_202_ACCEPTED,data=data)       