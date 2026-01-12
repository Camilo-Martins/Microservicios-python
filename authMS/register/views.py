from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import *
from .services.registro_service import*

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
                    'nombre': openapi.Schema(type=openapi.TYPE_STRING, description="nombre"),
                    'nombre_tienda': openapi.Schema(type=openapi.TYPE_STRING, description="nombre de la tienda a registrar"),
                    'password': openapi.Schema(type=openapi.TYPE_STRING, description="password")
                },
                required=['email', 'nombre','nombre_tienda', 'password']
            ))
    def post(self, request):
        
        try:
            registro_admin(data=request.data)
            return JsonResponse({"estado":"ok", "msg":"Registro exitoso"}, status=HTTPStatus.OK)
        
        except  ValidationError as e:
            return JsonResponse({"estado":"error", "msg": str(e)}, status=HTTPStatus.BAD_REQUEST)
        
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno"},status=HTTPStatus.INTERNAL_SERVER_ERROR)


class ValidarCuenta(APIView):
    @swagger_auto_schema(
    operation_description="Endpoint registro",
    responses={
        200:"Success",
        409:"Conflict",
        500: "Internal Server Error"
    },)
    def post(selft, request, token):

        try:
            verificar_cuenta(token=token)            
            return JsonResponse({"estado":"ok", "msg":"Cuenta verificada correctamente"}, status=HTTPStatus.OK)
        
        except  ValidationError as e:
            return JsonResponse({"estado":"error", "msg": str(e)}, status=HTTPStatus.BAD_REQUEST)
        
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno"},status=HTTPStatus.INTERNAL_SERVER_ERROR)


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
        try:
            result = login_usuario(data=request.data)
            return JsonResponse({"token": result}, status=200)

        except  ValidationError as e:
            return JsonResponse({"estado":"error", "msg": str(e)}, status=HTTPStatus.BAD_REQUEST)
        
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno"},status=HTTPStatus.INTERNAL_SERVER_ERROR)



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
            
        try:
            recuperar_password(request.data)
            return JsonResponse({"estado":"correo enviado", "mensaje": "OK"}, status=HTTPStatus.OK)
        
        except  ValidationError as e:
            return JsonResponse({"estado":"error", "msg": str(e)}, status=HTTPStatus.BAD_REQUEST)
        
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno"},status=HTTPStatus.INTERNAL_SERVER_ERROR)
        

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
        
        try:
            cambiar_password(request.data,token)
            return JsonResponse({"estado":"correo enviado", "mensaje": "OK"}, status=HTTPStatus.OK)
        
        except  ValidationError as e:
            return JsonResponse({"estado":"error", "msg": str(e)}, status=HTTPStatus.BAD_REQUEST)
        
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno"},status=HTTPStatus.INTERNAL_SERVER_ERROR)
        
