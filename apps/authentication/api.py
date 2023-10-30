from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.api.mixins import ApiAuthMixin
from apps.authentication.serializers.input_serializer import InputSerializer

from apps.authentication.services import auth_logout
from apps.users.selectors import user_get_login_data

# import from doc
from apps.docs.authentication.jwt.requests import REQUEST_AUTHENTICATION_LOGIN_JWT, REQUEST_AUTHENTICATION_LOGOUT_JWT
from apps.docs.authentication.jwt.responses import  RESPONSE_AUTHENTICATION_LOGIN_JWT, RESPONSE_AUTHENTICATION_LOGOUT_JWT
from apps.docs.authentication.me.responses import RESPONSE_ME
from apps.docs.authentication.session.requests import REQUEST_AUTHENTICATION_LOGIN_SESSION
from apps.docs.authentication.session.response import RESPONSE_AUTHENTICATION_LOGIN_SESSION



class UserSessionLoginApi(APIView):
    
    """
        Rota para realizar o login usando sessões de autenticação do Django.

        Esta rota permite aos usuários autenticarem-se no sistema usando o método de autenticação
        por sessão do Django. Ela segue o fluxo padrão de autenticação do Django e usa um serializer
        personalizado para validar os dados de entrada.

        Esta rota segue o método de autenticação padrão do Django e permite que os usuários iniciem uma sessão autenticada no sistema. Certifique-se de fornecer as credenciais corretas para autenticar com sucesso.
    """
    
    input_Serializer = InputSerializer
    @swagger_auto_schema(
        operation_description='''Rota para realizar o login usando sessões de autenticação do Django.
      
        #Usuario padrão
        email:admin@admin.com
        password:admin
        
        
        Esta rota permite aos usuários autenticarem-se no sistema usando o método de autenticação
        por sessão do Django. Ela segue o fluxo padrão de autenticação do Django e usa um serializer
        personalizado para validar os dados de entrada.''',
        request_body=REQUEST_AUTHENTICATION_LOGIN_SESSION,
        responses=RESPONSE_AUTHENTICATION_LOGIN_SESSION
    )
    def post(self, request):
        serializer = self.input_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(request, **serializer.validated_data)

        if user is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        login(request, user)

        data = user_get_login_data(user=user)
        session_key = request.session.session_key

        return Response({"session": session_key, "data": data})

class UserSessionLogoutApi(APIView):
    """
        Rota para realizar o logout e encerrar a sessão do usuário.

        Esta rota permite aos usuários encerrarem sua sessão ativa no sistema. Isso revoga o
        acesso autenticado e encerra a sessão do usuário.


        Utilize esta rota para encerrar a sessão ativa do usuário e efetuar o logout com segurança.
    """
    
    
    @swagger_auto_schema(
        operation_description="Utilize esta rota para encerrar a sessão ativa do usuário e efetuar o logout com segurança.",
        responses={200: "Sessão encerrada com sucesso."}
        )
    def post(self, request):
        logout(request)

        return Response()
    
    def get(self, request):
        logout(request)

        return Response()

class UserJwtLoginApi(TokenObtainPairView):
    
    """
        Rota para realizar o login usando JWT (JSON Web Token).

        Esta rota permite aos usuários autenticarem-se no sistema e obter um token JWT válido
        para acessar recursos protegidos.
    """


    @swagger_auto_schema(
        request_body=REQUEST_AUTHENTICATION_LOGIN_JWT,
        operation_description='''Esta rota permite aos usuários autenticarem-se no sistema e obter um token JWT válido para acessar recursos protegidos.
        
        #Usuario padrão
        email:admin@admin.com
        password:admin
        ''',
        responses=RESPONSE_AUTHENTICATION_LOGIN_JWT
        )  
    def post(self, request, *args, **kwargs):
        # We are redefining post so we can change the response status on success
        # Mostly for consistency with the session-based API
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_201_CREATED:
            response.status_code = status.HTTP_200_OK

        return response

class UserJwtLogoutApi(ApiAuthMixin, APIView):
    """
        Rota para realizar o logout e revogar tokens JWT de um usuário autenticado.

        Esta rota permite aos usuários encerrarem sua sessão ativa no sistema e revogarem os tokens
        JWT associados à sua autenticação.
    
    """
    @swagger_auto_schema(
        operation_description='''Esta rota permite aos usuários encerrarem sua sessão ativa no sistema e revogarem os tokens JWT associados à sua autenticação.''',
        request_body=REQUEST_AUTHENTICATION_LOGOUT_JWT,
        responses=RESPONSE_AUTHENTICATION_LOGOUT_JWT
    )
    def post(self, request):
 
        auth_logout(request.user,request.data.get("refresh"))
        response = Response()

        return response

class UserMeApi(ApiAuthMixin, APIView):
    """
        Rota para obter informações do usuário autenticado.

        Esta rota permite aos usuários autenticados obter informações sobre sua própria conta, como nome de usuário,
        email e outros detalhes relacionados.
    
    """
    @swagger_auto_schema(
        operation_description='''Esta rota permite aos usuários autenticados obter informações sobre sua própria conta, como nome de usuário,email e outros detalhes relacionados.''',
        responses=RESPONSE_ME
    )
    def get(self, request):
        data = user_get_login_data(user=request.user)

        return Response(data)