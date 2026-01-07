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
            dias = data.dias.all()
            datos_json= DiaHorarioSerializer(dias, many=True).data
       

            return JsonResponse({"data":{"id": data.id, "nombre":data.nombre,
                                            "fecha_inicio" :data.fecha_inicio,
                                            "fecha_fin":data.fecha_fin,
                                            "is_active":data.is_active, 
                                            "admin_id":data.admin_id,
                                            "dias": datos_json,
                                         } }, 
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

            horario = HorarioSemanal.objects.create(
                nombre=nombre,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin,
                admin_id=resuelto["id"]
            )

            for dia in range(1,7):
                DiaHorario.objects.create(
                    horario=horario,
                    dia=dia
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
                                        is_active=False)
            return JsonResponse({"estado":"ok", "msg":"Horario desactivado"}, status=HTTPStatus.OK)
        except Exception as e:
            return JsonResponse({"estado":"error", "msg":"Hubo un error al modificar el emplado"}, status=HTTPStatus.BAD_REQUEST)


class AsignacioEmpleadoHorario(APIView):
    @logueado()
    def post(self, request, horario_id):

        #Validacion de admin
        header = request.headers.get('Authorization').split(" ")
        resuelto=jwt.decode(header[1], os.getenv("SECRET_KEY"), algorithms=['HS512'] )

        #Filtrar por horario ID y Active = True
        if not HorarioSemanal.objects.filter(admin_id=resuelto["id"], id=horario_id, is_active=True).exists():
            return JsonResponse({"estado":"error", "msg":"Recuerdo no encontrado u horario desactivado"}, 
                                status=HTTPStatus.BAD_REQUEST)
        
        #Validar que el dia no tenga mas de dos Empleados Asociados

        #Validar que no se repita el mismo empleado

        try:
            return
        except Exception as e:
            return
        

class AsignarSemana(APIView):
    @logueado()

    
    def post(self, request, id):

         #Validacion de admin
        header = request.headers.get('Authorization').split(" ")
        resuelto=jwt.decode(header[1], os.getenv("SECRET_KEY"), algorithms=['HS512'] )

        admin_id = resuelto["id"]
        asignaciones = request.data.get("asignaciones")

        if not asignaciones:
            return JsonResponse(
                {"estado": "error", "msg": "No hay asignaciones"},
                status=HTTPStatus.BAD_REQUEST
            )

        # 1. Horario válido
        try:
            horario = HorarioSemanal.objects.get(
                id=id,
                admin_id=admin_id,
                is_active=True
            )
        except HorarioSemanal.DoesNotExist:
            return JsonResponse(
                {"estado": "error", "msg": "Horario no válido"},
                HTTPStatus.BAD_REQUEST
            )

        # 2. Iterar días
        for dia_num, empleados in asignaciones.items():

            try:
                dia = DiaHorario.objects.get(
                    horario=horario,
                    dia=int(dia_num)
                )
            except DiaHorario.DoesNotExist:
                return JsonResponse(
                    {"estado": "error", "msg": f"Día {dia_num} no válido"},
                    status=400
                )

            # 3. Iterar empleados
            for empleado_id in empleados:
                error = asignar_empleado_a_dia(
                    admin_id=admin_id,
                    dia=dia,
                    empleado_id=empleado_id
                )

                if error:
                    return JsonResponse(
                        {"estado": "error", "msg": error},
                        status=400
                    )

        return JsonResponse(
            {"estado": "ok", "msg": "Asignaciones creadas"},
            status=201
        )
