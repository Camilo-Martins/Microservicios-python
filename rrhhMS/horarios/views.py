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
    def get(self, request):
        try:
            admin_id = get_admin_id_from_request(request)
        except Exception as e:
            return JsonResponse({"estado":"error", "mensaje":"Recurso no disponible"}, status=HTTPStatus.NOT_FOUND)


        serializer = GetHorarioSerializer(data={"admin_id":admin_id})
        serializer.is_valid(raise_exception=True)

        horario, dias = GetHorarioService.obtener_horario(
            admin_id=admin_id
        )

        data = {
            "horario" : HorarioSerializer(horario).data,
        }

        return JsonResponse(data,status=HTTPStatus.OK)
       

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
        
        try:
            admin_id = get_admin_id_from_request(request)
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno"},status=HTTPStatus.INTERNAL_SERVER_ERROR)
       
        serializer = CreateHorarioSerializer(data={"admin_id":admin_id})
        serializer.is_valid(raise_exception=True)

        data = CreateHorarioService.crear_horario(
            admin_id=admin_id
        )
        
        return JsonResponse(
                {"estado": "ok", "msg": "Horario Creado"},
                status=201
            )


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
        except Exception:
            return JsonResponse( {"estado": "error", "msg": "Error interno"}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

         
        serializer = AsignarDiaSerializer(data={"admin_id":admin_id, "id":id,  "data":request.data})
        serializer.is_valid(raise_exception=True)

        data = AsignarPersonalService.asignar_semana(
                admin_id=admin_id,
                id=id,
                dia=request.data.get("dia"),
                personal=request.data.get("personal"),
        )
        
        return JsonResponse(
                {"estado": "ok", "msg": "Horario Creado"},
                status=201
            )


class DesasignarSemana(APIView):
    @logueado()

   
    def post(self, request, id):
        try:
            admin_id = get_admin_id_from_request(request)
        except Exception:
            return JsonResponse( {"estado": "error", "msg": "Error interno"}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

        print(id, request.data)
         
        serializer = AsignarDiaSerializer(data={"admin_id":admin_id, "id":id,  "data":request.data})
        serializer.is_valid(raise_exception=True)

        data = DesasginarPersonalService.desasginar_semana(
                admin_id=admin_id,
                id=id,
                dia=request.data.get("dia"),
                personal=request.data.get("personal"),
        )
        
        return JsonResponse(
                {"estado": "ok", "msg": "Horario Creado"},
                status=201
            )