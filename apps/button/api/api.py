from rest_framework.views import APIView
from rest_framework.response import Response
from apps.api.pagination import LimitOffsetPagination, get_paginated_response
from apps.button.selectors.selector import button_get, button_list
from rest_framework import status
from apps.button.serializers.filter_serializer import ButtonFilterSerializer
from apps.button.serializers.input_serializer import ButtonUpdateInputSerializer

from apps.button.serializers.output_serializer import ButtonOutputSerializer
from apps.button.service.button import button_create, button_update

from apps.api.mixins import ApiAuthMixin

from apps.button.models import Button

class ButtonListApi(ApiAuthMixin,APIView):
    
    class Pagination(LimitOffsetPagination):
        default_limit = 20

    output_serializer = ButtonOutputSerializer
    filter_serializer = ButtonFilterSerializer
  
    def get(self, request):
        
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
    
    def get(self,request,button_id):
       button: Button =  button_get(id=button_id)
       
       if button is None:
           return Response(status=status.HTTP_400_BAD_REQUEST)
       
       data = self.output_serializer(button).data
       
       return Response(status=status.HTTP_200_OK,data=data)


class ButtonCreateApi(ApiAuthMixin,APIView):
    
    output_serializer = ButtonOutputSerializer
    
    def post(self,request):
        
        button = button_create(user=request.user)
        data = self.output_serializer(button).data
        return Response(status=status.HTTP_201_CREATED,data=data)

class ButtonUpdateApi(ApiAuthMixin, APIView):
    
    input_serializer = ButtonUpdateInputSerializer
    output_serializer = ButtonOutputSerializer
    
    def patch(self, request, button_id):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        button = button_get(id=button_id)
        if button is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        school_new = button_update(button=button,data=serializer.validated_data)
        data = self.output_serializer(school_new).data
        return Response(status=status.HTTP_202_ACCEPTED,data=data)       