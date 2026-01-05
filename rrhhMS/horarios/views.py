from django.shortcuts import render
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
from .serializers import*

#Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.


#HORARIO

class ObtenerHorarios(APIView):  
    @logueado()
    @swagger_auto_schema(
            operation_description="Endpoint Obtener horarios",
            responses={
                200:"Success",
                400:"Bad Request"
            },
    )
    def get(self, request):
        header = request.headers.get('Authorization').split(" ")
        resuelto=jwt.decode(header[1], os.getenv("SECRET_KEY"), algorithms=['HS512'] )

        data = HorarioSemanal.objects.filter(admin_id=resuelto["id"]).order_by('id').all()
        datos_json= HorarioSerializer(data, many=True)
        return JsonResponse({"data":datos_json.data})

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
        header = request.headers.get('Authorization').split(" ")
        resuelto=jwt.decode(header[1], os.getenv("SECRET_KEY"), algorithms=['HS512'] )

        try:
            
            data = HorarioSemanal.objects.filter(admin_id=resuelto["id"], id=id).get()
            return JsonResponse({"data":{"id": data.id, "nombre":data.nombre,
                                            "fecha_inicio" :data.fecha_inicio,
                                            "fecha_fin":data.fecha_fin,
                                            "is_active":data.is_active, 
                                            "admin_id":data.admin_id}}, 
                                    status=HTTPStatus.OK)
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

        header = request.headers.get('Authorization').split(" ")
        resuelto=jwt.decode(header[1], os.getenv("SECRET_KEY"), algorithms=['HS512'] )

        fecha_inicio = date.today()
        fecha_fin = fecha_inicio + timedelta(days=5)
        
        inicio_str = date_format(fecha_inicio, "d/m/Y")
        fin_str = date_format(fecha_fin, "d/m/Y")

        nombre = f"Horario semana {inicio_str} - {fin_str}"

        if HorarioSemanal.objects.filter(admin_id=resuelto["id"], nombre=nombre, is_active=True).exists():
            return JsonResponse({"estado":"error", "msg":"Ya existe un horario para esta semana."}, status=HTTPStatus.BAD_REQUEST)

        try:

            HorarioSemanal.objects.create(
                nombre=nombre,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin,
                admin_id=resuelto["id"]
            )
            return JsonResponse({"estado":"ok", "msg":"Horario creado"}, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({"estado":"error", "mensaje": "Error al crear horario"}, status=HTTPStatus.NOT_FOUND)

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

        header = request.headers.get('Authorization').split(" ")
        resuelto=jwt.decode(header[1], os.getenv("SECRET_KEY"), algorithms=['HS512'] )

        try:
            data = HorarioSemanal.objects.filter(admin_id=resuelto["id"], id=id).get()
        except HorarioSemanal.DoesNotExist:
            return JsonResponse({"estado":"error", "mensaje":"Recurso no disponible"}, status=HTTPStatus.NOT_FOUND)
        

        try:
            HorarioSemanal.objects.filter(admin_id=resuelto["id"], id=id).update(
                                        is_active=False,)
            return JsonResponse({"estado":"ok", "msg":"Horario desactivado"}, status=HTTPStatus.OK)
        except Exception as e:
            return JsonResponse({"estado":"error", "msg":"Hubo un error al modificar el emplado"}, status=HTTPStatus.BAD_REQUEST)
