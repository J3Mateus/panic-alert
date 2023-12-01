from email.headerregistry import Address
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.button.selectors.selector import button_get
from rest_framework import status

from apps.button.serializers.output_serializer import ButtonOutputSerializer
from apps.button.service.button import button_create

from apps.api.mixins import ApiAuthMixin

from apps.button.models import Button

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

       