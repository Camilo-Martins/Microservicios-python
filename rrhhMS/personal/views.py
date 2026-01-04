from django.shortcuts import render

from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404
from .models.empleado import*
from django.utils.dateformat import DateFormat
from dotenv import load_dotenv
import os
from datetime import datetime
from jose import jwt

from decorators.decorators import logueado
from .serializers import EmpleadoSerializer
# Create your views here.

class Clasel(APIView):

    @logueado()
    def get(self, request):

        header = request.headers.get('Authorization').split(" ")
        resuelto=jwt.decode(header[1], os.getenv("SECRET_KEY"), algorithms=['HS512'] )

        data = Empleado.objects.filter(admin_id=resuelto["id"]).order_by('id').all()
        datos_json= EmpleadoSerializer(data, many=True)
        return JsonResponse({"data":datos_json.data})
    

    @logueado()
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



    @logueado()
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
            return JsonResponse({"estado":"error", "msg":"Ya existe un empleado asociado a este telefono"}, status=HTTPStatus.BAD_REQUEST)


            #Validación usuario unico
        if Empleado.objects.filter(telefono=request.data["rut"]).exists():
            return JsonResponse({"estado":"error", "msg":"Ya existe un empleado asociado a este rut"}, status=HTTPStatus.BAD_REQUEST)


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
            return JsonResponse({"estado":"error", "msg":"Ya existe un empleado asociado a este telefono"}, status=HTTPStatus.BAD_REQUEST)


    @logueado()
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
        
    @logueado()
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
