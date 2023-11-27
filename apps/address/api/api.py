from email.headerregistry import Address
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.address.selectors.address import address_get_api
from rest_framework import status
from apps.address.serializers.input_serializer import AddressInputSerializer
from apps.address.serializers.output_serializer import AddressOutputSerializer
from apps.address.service.address import address_create

from apps.api.mixins import ApiAuthMixin


class AdressDetailApi(ApiAuthMixin,APIView):
    
    output_serializer = AddressOutputSerializer
    
    def get(self,request,cep):
       address: Address =  address_get_api(cep)
       
       if address is None:
           return Response(status=status.HTTP_400_BAD_REQUEST)
       
       data = self.output_serializer(address).data
       
       return Response(status=status.HTTP_200_OK,data=data)


class AddressCreateApi(ApiAuthMixin,APIView):
    
    input_serializer = AddressInputSerializer
    output_serializer = AddressOutputSerializer
    
    def post(self,request):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        school = address_create(**serializer.validated_data,user=request.user)
        data = self.output_serializer(school).data
        return Response(status=status.HTTP_201_CREATED,data=data)

       