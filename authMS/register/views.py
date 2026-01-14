from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import *
from .services.registro_service import*
from .serializers import RegisterStoreSerializer
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


