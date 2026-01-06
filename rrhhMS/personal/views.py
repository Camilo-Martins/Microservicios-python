from django.shortcuts import render

from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404
from .models.empleado import*
from .models.asistencia import*
from django.utils.dateformat import DateFormat
from horarios.models import*
from dotenv import load_dotenv
import os
from datetime import datetime
from jose import jwt
from datetime import timedelta
from decorators.decorators import logueado
from .serializers import EmpleadoSerializer

#Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Create your views here.

class ObtenerEmpleados(APIView):
    @logueado()
    @swagger_auto_schema(
            operation_description="Endpoint Obtener Empleados",
            responses={
                200:"Success",
                400:"Bad Request"
            },
          
    )
    def get(self, request):

        header = request.headers.get('Authorization').split(" ")
        resuelto=jwt.decode(header[1], os.getenv("SECRET_KEY"), algorithms=['HS512'] )

        data = Empleado.objects.filter(admin_id=resuelto["id"]).order_by('id').all()
        datos_json= EmpleadoSerializer(data, many=True)
        return JsonResponse({"data":datos_json.data})
    
class ObtenerEmpleado(APIView):
    @logueado()
    @swagger_auto_schema(
            operation_description="Endpoint Obtener Empleado",
            responses={
                200:"Success",
                400:"Bad Request"
            }
    )
    def get(self, request,id):

        header = request.headers.get('Authorization').split(" ")
        resuelto=jwt.decode(header[1], os.getenv("SECRET_KEY"), algorithms=['HS512'] )

        try:
            data = Empleado.objects.filter(admin_id=resuelto["id"], id=id).get()
            return JsonResponse({"data":{"id": data.id, "nombre_completo":data.nombre_completo,
                                         "created_at":DateFormat(data.created_at).format('d/m/Y'), "rol":data.rol,
                                         "pago_diario":data.pago_diario,
                                         "telefono":data.telefono,
                                         "is_active":data.is_active, 
                                         "admin_id":data.admin_id}}, 
                                status=HTTPStatus.OK)
        except Exception as e:
            return JsonResponse({"estado":"error", "mensaje":"Recurso no disponible"}, status=HTTPStatus.NOT_FOUND)

class RegistroEmpleado(APIView):
    @logueado()
    @swagger_auto_schema(
            operation_description="Endpoint Registro Empleado",
            responses={
                200:"Success",
                400:"Bad Request"
            },
            request_body=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'nombre_completo': openapi.Schema(type=openapi.TYPE_STRING, description="nombre_completo"),
                    'telefono': openapi.Schema(type=openapi.TYPE_STRING, description="telefono"),
                    'rol': openapi.Schema(type=openapi.TYPE_STRING, description="rol"),
                    'medio_pago': openapi.Schema(type=openapi.TYPE_STRING, description="medio_pago"),
                    'pago_diario': openapi.Schema(type=openapi.TYPE_INTEGER, description="pago_diario"),
                    'rut': openapi.Schema(type=openapi.TYPE_STRING, description="rut")
                },
                required=['nombre_completo', 'telefono', 'rol', 'pago_diario', 'rut']
            )
    )
    def post(self, request):

        header = request.headers.get('Authorization').split(" ")
        resuelto=jwt.decode(header[1], os.getenv("SECRET_KEY"), algorithms=['HS512'] )

          #Validaciones generales
        if request.data.get("nombre_completo") == None or not request.data.get("nombre_completo"):
            return JsonResponse({"estado": "error", "msg":"El campo nombre es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("telefono") == None or not request.data.get("telefono"):
            return JsonResponse({"estado": "error", "msg":"El campo telefono es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("rol") == None or not request.data.get("rol"):
            return JsonResponse({"estado": "error", "msg":"El campo rol es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("pago_diario") == None or not request.data.get("pago_diario"):
            return JsonResponse({"estado": "error", "msg":"El campo pago_diario es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("rut") == None or not request.data.get("rut"):
            return JsonResponse({"estado": "error", "msg":"El campo rut es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        
        #Validación usuario unico
        if Empleado.objects.filter(telefono=request.data["telefono"]).exists():
            return JsonResponse({"estado":"error", "msg":request.data["telefono"] }, status=HTTPStatus.BAD_REQUEST)


            #Validación usuario unico
        if Empleado.objects.filter(rut=request.data["rut"]).exists():
            return JsonResponse({"estado":"error", "msg":request.data["rut"]}, status=HTTPStatus.BAD_REQUEST)


        try:
            Empleado.objects.create(nombre_completo=request.data["nombre_completo"], 
                                        telefono=request.data["telefono"], 
                                        rol=request.data["rol"], 
                                        is_active=True,
                                        rut=request.data["rut"],
                                        medio_pago=request.data["medio_pago"],
                                        pago_diario=request.data["pago_diario"],
                                        admin_id=resuelto["id"])
            return JsonResponse({"estado":"ok", "msg":"Registro exitoso"}, status=HTTPStatus.OK)
        except Exception as e:
            return JsonResponse({"estado":"error", "msg":"Error!"}, status=HTTPStatus.BAD_REQUEST)

class DesactivarEmpleado(APIView):
    @logueado()
    @swagger_auto_schema(
            operation_description="Endpoint Desactivar Empleado",
            responses={
                200:"Success",
                400:"Bad Request"
            },
    )
    def patch(self, request, id):

        header = request.headers.get('Authorization').split(" ")
        resuelto=jwt.decode(header[1], os.getenv("SECRET_KEY"), algorithms=['HS512'] )

        try:
            data = Empleado.objects.filter(admin_id=resuelto["id"], id=id).get()
        except Empleado.DoesNotExist:
            return JsonResponse({"estado":"error", "mensaje":"Recurso no disponible"}, status=HTTPStatus.NOT_FOUND)
        

        try:
            Empleado.objects.filter(admin_id=resuelto["id"], id=id).update(
                                        is_active=False,)
            return JsonResponse({"estado":"ok", "msg":"Empleado desactivado"}, status=HTTPStatus.OK)
        except Exception as e:
            return JsonResponse({"estado":"error", "msg":"Hubo un error al modificar el emplado"}, status=HTTPStatus.BAD_REQUEST)


class EditarEmpleado(APIView):
    @logueado()
    @swagger_auto_schema(
            operation_description="Endpoint Editar Empleado",
            responses={
                200:"Success",
                400:"Bad Request"
            },
            request_body=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'nombre_completo': openapi.Schema(type=openapi.TYPE_STRING, description="nombre_completo"),
                    'telefono': openapi.Schema(type=openapi.TYPE_STRING, description="telefono"),
                    'rol': openapi.Schema(type=openapi.TYPE_STRING, description="rol"),
                    'pago_diario': openapi.Schema(type=openapi.TYPE_STRING, description="pago_diario"),
                    'rut': openapi.Schema(type=openapi.TYPE_STRING, description="rut")
                },
                required=['nombre_completo', 'telefono', 'rol', 'pago_diario', 'rut']
            )
    )
    def put(self, request, id):

        header = request.headers.get('Authorization').split(" ")
        resuelto=jwt.decode(header[1], os.getenv("SECRET_KEY"), algorithms=['HS512'] )

        try:
            data = Empleado.objects.filter(admin_id=resuelto["id"], id=id).get()
        except Empleado.DoesNotExist:
            return JsonResponse({"estado":"error", "mensaje":"Recurso no disponible"}, status=HTTPStatus.NOT_FOUND)
        
            #Validaciones generales
        if request.data.get("nombre_completo") == None or not request.data.get("nombre_completo"):
            return JsonResponse({"estado": "error", "msg":"El campo nombre es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("telefono") == None or not request.data.get("telefono"):
            return JsonResponse({"estado": "error", "msg":"El campo telefono es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("rol") == None or not request.data.get("rol"):
            return JsonResponse({"estado": "error", "msg":"El campo rol es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("pago_diario") == None or not request.data.get("pago_diario"):
            return JsonResponse({"estado": "error", "msg":"El campo pago_diario es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        
        if request.data.get("rut") == None or not request.data.get("rut"):
            return JsonResponse({"estado": "error", "msg":"El campo rut es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        
        #Validación usuario unico
        if Empleado.objects.filter(telefono=request.data["telefono"]).exists():
            return JsonResponse({"estado":"error", "msg":"Ya existe un empleado asociado a este telefono"}, status=HTTPStatus.BAD_REQUEST)


            #Validación usuario unico
        if Empleado.objects.filter(telefono=request.data["rut"]).exists():
            return JsonResponse({"estado":"error", "msg":"Ya existe un empleado asociado a este rut"}, status=HTTPStatus.BAD_REQUEST)


        try:
            Empleado.objects.filter(admin_id=resuelto["id"], id=id).update(nombre_completo=request.data["nombre_completo"], 
                                        telefono=request.data["telefono"], 
                                        rol=request.data["rol"], 
                                        is_active=True,
                                        rut=request.data["rut"],
                                        medio_pago=request.data["medio_pago"],
                                        pago_diario=request.data["pago_diario"],
                                        admin_id=resuelto["id"])
            return JsonResponse({"estado":"ok", "msg":"Empleado actualizado"}, status=HTTPStatus.OK)
        except Exception as e:
            return JsonResponse({"estado":"error", "msg":"Hubo un error al modificar el emplado"}, status=HTTPStatus.BAD_REQUEST)
        


class AsistenciaEmpleado(APIView):
    @logueado()
    def post(self, request, id):

        header = request.headers.get('Authorization').split(" ")
        resuelto=jwt.decode(header[1], os.getenv("SECRET_KEY"), algorithms=['HS512'] )

        #Validar si horario existe
        try:
            horario = HorarioSemanal.objects.filter(admin_id=resuelto["id"], id=id).get()
        except HorarioSemanal.DoesNotExist:
            return JsonResponse({"estado":"error", 
                                "mensaje":"Recurso no disponible"}, 
                                status=HTTPStatus.NOT_FOUND)


        try:
            empleado = Empleado.objects.filter(id=request.data["empleado_id"]).get()
        except HorarioSemanal.DoesNotExist:
            return JsonResponse({"estado":"error", 
                                "mensaje":"Recurso no disponible"}, 
                                status=HTTPStatus.NOT_FOUND)


        #Recibir el dia e id del empleado
        fecha_asistencia = horario.fecha_inicio + timedelta(days=request.data["dia"] - 1)
      
        try:
            Asistencia.objects.create(
                    empleado=empleado, 
                    asistio = request.data["asistencia"],
                    fecha = fecha_asistencia

            )
            return JsonResponse({"estado":"ok", "msg":"Asistencia Registrada"}, status=HTTPStatus.OK)
        except Exception as e:
            return JsonResponse({"estado":"error", "msg":"Hubo un error al registrar asistencia"}, status=HTTPStatus.BAD_REQUEST)