from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404
from django.utils.dateformat import DateFormat
from django.utils.formats import date_format
from dotenv import load_dotenv
import os
from datetime import datetime, date, timedelta
from jose import jwt

from decorators.decorators import logueado
from .models.horario_semana import*
from .models.dia_horario import*
from .serializers import*
from helpers.asignaciones import asignar_empleado_a_dia
from .utils.auth import get_admin_id_from_request

#Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
from .services.horario_service import*


#HORARIO

class ObtenerHorarios(APIView):  
    @logueado()
    @swagger_auto_schema(
            operation_description="Endpoint Obtener horarios",
            responses={
                200:"Success",
                400:"Bad Request"
            }
    )
    def get(self, request):

        try:
            admin_id = get_admin_id_from_request(request)
            horarios = obtener_horarios_por_admin(admin_id)

            datos_json= HorarioSerializer(horarios, many=True)
            return JsonResponse({"data":datos_json.data})
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Horario no encontrado"}, status=400)

class ObtenerHorario(APIView):
    @logueado()
    @swagger_auto_schema(
            operation_description="Endpoint Obtener horario por ID",
            responses={
                200:"Success",
                400:"Bad Request"
            },
    )
    def get(self, request,id):
        try:
            admin_id = get_admin_id_from_request(request)

            horario, dias = obtener_horario_por_admin(admin_id,id)


            data = {
                "horario" : HorarioSerializer(horario).data,
                 "dias" : DiaHorarioSerializer(dias, many=True).data,
            }

            return JsonResponse(data,status=HTTPStatus.OK)
        except Exception as e:
            return JsonResponse({"estado":"error", "mensaje":"Recurso no disponible"}, status=HTTPStatus.NOT_FOUND)

class CrearHorario(APIView):
    @logueado()
    @swagger_auto_schema(
            operation_description="Endpoint Creacion Horario ( Forma automatica )",
            responses={
                200:"Success",
                400:"Bad Request"
            },
    )
    def post(self, request):

        admin_id = get_admin_id_from_request(request)
      
        try:
            crear_horario(admin_id, request.data)
            return JsonResponse({"estado":"ok", "msg":"Horario creado"}, status=HTTPStatus.OK)

        except  ValidationError as e:
            return JsonResponse({"estado":"error", "msg": str(e)}, status=HTTPStatus.NOT_FOUND)
        
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno"},status=HTTPStatus.INTERNAL_SERVER_ERROR)

class DesactivarHorario(APIView):
    @logueado()
    @swagger_auto_schema(
            operation_description="Endpoint Desactivar Horario (Forma automatica)",
            responses={
                200:"Success",
                400:"Bad Request"
            },
    )
    def patch(self, request, id):

        admin_id = get_admin_id_from_request(request)

        try:
            desactivar_horario(admin_id,id)

            return JsonResponse({"estado":"ok", "msg":"Horario desactivado"}, status=HTTPStatus.OK)
        
        except ValidationError as e:
            return JsonResponse({"estado":"error", "msg": e}, status=HTTPStatus.BAD_REQUEST)
            
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno"},status=HTTPStatus.INTERNAL_SERVER_ERROR)


class AsignarSemana(APIView):
    @logueado()

   
    def post(self, request, id):
        try:
            admin_id = get_admin_id_from_request(request)
            asignar_semana(admin_id, id, request.data)

            return JsonResponse(
                {"estado": "ok", "msg": "Asignaciones creadas"},
                status=HTTPStatus.CREATED
            )

        except ValidationError as e:
            return JsonResponse(
                {"estado": "error", "msg": str(e)},
                status=HTTPStatus.BAD_REQUEST
            )

        except Exception:
            return JsonResponse(
                {"estado": "error", "msg": "Error interno"},
                status=HTTPStatus.INTERNAL_SERVER_ERROR
            )