from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import *
from .services.registro_service import*
from .serializers import RegisterStoreSerializer, ConfirmAccountSerializer, LoginSerializer, ResetPassSerielizer, NewPassSerielizer
# Create your views here.

class RegistroUsuario(APIView):
    @swagger_auto_schema(
            operation_description="Endpoint registro",
            responses={
                200:"Success",
                409:"Conflict",
                500: "Internal Server Error"
            },
            request_body=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'email': openapi.Schema(type=openapi.TYPE_STRING, description="email"),
                    'username': openapi.Schema(type=openapi.TYPE_STRING, description="username"),
                    'nombre_tienda': openapi.Schema(type=openapi.TYPE_STRING, description="nombre de la tienda a registrar"),
                    'password': openapi.Schema(type=openapi.TYPE_STRING, description="password")
                },
                required=['email', 'username','nombre_tienda', 'password']
            ))
    def post(self, request):

        serializer = RegisterStoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        RegisterService.registro_admin(
            **serializer.validated_data
        )

        return JsonResponse(
            {"estado": "ok", "msg": "Registro exitoso"},
            status=HTTPStatus.OK
        )


class ValidarCuenta(APIView):
    @swagger_auto_schema(
    operation_description="Endpoint Confirmar Cuenta",
    responses={
        200:"Success",
        409:"Conflict",
        500: "Internal Server Error"
    },)
    def post(selft, request, token):
        
        serializer = ConfirmAccountSerializer(data={"token":token})
        serializer.is_valid(raise_exception=True)

        ConfirmService.confirm_account(
          token=token
        )

        return JsonResponse({"estado":"ok", "msg":"Cuenta verificada correctamente"}, status=HTTPStatus.OK)
        

class Login(APIView):
    @swagger_auto_schema(
        operation_description="Endpoint login",
        responses={
            200:"Success",
            409:"Conflict",
            500: "Internal Server Error"
        },
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description="email"),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description="password")
            },
            required=['email', 'password']
    ))
    def post(self,request):       
      
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = LoginService.login(
            **serializer.validated_data
        )
        
        return JsonResponse({"token":result}, status=HTTPStatus.OK)
      

class RecuperarPassword(APIView):
    @swagger_auto_schema(
        operation_description="Endpoint recuperar contraseña",
        responses={
            200:"Success",
            409:"Conflict",
            500: "Internal Server Error"
        },
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description="email"),
            
            },
            required=['email']
    ))
    def post(self,request):
            
        serializer = ResetPassSerielizer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ResetPassService.resetPassword(
            **serializer.validated_data
        )
        
        return JsonResponse({"OK": "Mensaje enviado"}, status=HTTPStatus.OK)


class CambiarPassword(APIView):
    @swagger_auto_schema(
        operation_description="Endpoint cambiar contraseña",
        responses={
            200:"Success",
            409:"Conflict",
            500: "Internal Server Error"
        },
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'password': openapi.Schema(type=openapi.TYPE_STRING, description="password")
            },
            required=['password']
    ))
    def post(self,request,token):
        
        serializer = NewPassSerielizer(data={"token":token, "password": request.data["password"]})
        serializer.is_valid(raise_exception=True)

        NewPassService.new_pass(
          **serializer.validated_data
        )

        return JsonResponse({"estado":"ok", "msg":"Contraseña actualizada"}, status=HTTPStatus.OK)
        
