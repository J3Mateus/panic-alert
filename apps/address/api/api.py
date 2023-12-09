from email.headerregistry import Address
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.address.selectors.address import address_get_api
from rest_framework import status
from apps.address.serializers.input_serializer import AddressInputSerializer
from apps.address.serializers.output_serializer import AddressOutputSerializer
from apps.address.service.address import address_create
from drf_yasg.utils import swagger_auto_schema

from apps.api.mixins import ApiAuthMixin


class AdressDetailApi(ApiAuthMixin,APIView):
    
    output_serializer = AddressOutputSerializer
    @swagger_auto_schema(
        manual_parameters=[
            # Adicione parâmetros manuais, se necessário
        ],
        responses={
            status.HTTP_200_OK: AddressOutputSerializer(many=False),
            status.HTTP_400_BAD_REQUEST: "Requisição Inválida",
            # Adicione outras respostas conforme necessário
        },
        operation_summary="Obter Detalhes do Endereço",
        operation_description="Recupere os detalhes de um endereço específico com base no CEP fornecido.",
    )
    def get(self,request,cep):
       """
        Obtém detalhes de um endereço específico.

        :param request: O objeto de requisição.
        :param str cep: O CEP (Código Postal) para o endereço.

        :return: Detalhes do endereço.
       """
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

       