from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404
from django.core.exceptions import ValidationError

#Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

#Locales
from .utils.auth import get_admin_id_from_request
from .services.empleado_service import*
from decorators.decorators import logueado
from .serializers import*

# Create your views here.

class ObtenerEmpleados(APIView):
    @logueado()
    @swagger_auto_schema(
            operation_description="Endpoint Obtener Empleados",
            responses={
                200:"Success",
                400:"Bad Request"},)
    def get(self, request):

        try:
            admin_id = get_admin_id_from_request(request)
            empleados = obtener_empleados_por_admin(admin_id)

            datos_json= EmpleadoSerializer(empleados, many=True)
            return JsonResponse({"data":datos_json.data})
        
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Empleado no encontrado"}, status=400)


class ObtenerEmpleado(APIView):
    @logueado()
    @swagger_auto_schema(
            operation_description="Endpoint Obtener Empleado",
            responses={
                200:"Success",
                400:"Bad Request"})
    def get(self, request,id):

        try: 
            admin_id = get_admin_id_from_request(request)

            empleado, asistencias, pagos = obtener_empleado(admin_id, id)

            data = {
                "empleado": EmpleadoSerializer(empleado).data,
                "asistencias": AsistenciaSerializer(asistencias, many=True).data,
                "pagos": PagoSerializer(pagos, many=True).data,
            }

            return JsonResponse(data, status=200)
        except Http404:
            return JsonResponse({"estado": "error", "msg": "Empleado no encontrado"}, status=400)

        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno del servidor"},status=500)
        
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
    
        try:
            admin_id = get_admin_id_from_request(request)

            crear_empleado(
                admin_id= admin_id,
                data=request.data
            )

            return JsonResponse(
                {"estado": "ok", "msg": "Registro exitoso"},
                status=201
            )

        except Exception as e:
              return JsonResponse({"estado": "error", "msg":str(e)}, status=400)
        
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno"},status=500)


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

        admin_id = get_admin_id_from_request(request)

        try:
            nuevo_estado = desactivar_empleado(admin_id, id)
            msg = "Empleado activado" if nuevo_estado else "Empleado desactivado"

            return JsonResponse( {"estado": "ok", "msg": msg},status=200)

        except Http404:
            return JsonResponse({"estado": "error", "msg": "Empleado no encontrado"},status=404)

        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno"},status=500)


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

        admin_id = get_admin_id_from_request(request)

        try:
            editar_empleado(
                admin_id= admin_id,
                id=id,
                data=request.data
            )
            return JsonResponse({"estado":"ok", "msg":"Empleado actualizado"}, status=HTTPStatus.OK)
        except  ValidationError as e:
            return JsonResponse({"estado":"error", "msg": str(e)}, status=HTTPStatus.NOT_FOUND)
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno"},status=HTTPStatus.INTERNAL_SERVER_ERROR)
        

class AsistenciaEmpleado(APIView):
    @logueado()
    def post(self, request, id):

        admin_id = get_admin_id_from_request(request)
      
        try:
            asistencia_empleado(admin_id,id, data=request.data)

            return JsonResponse(
                {"estado": "ok", "msg": "Registro exitoso"}, status=201)

        except Exception:
              return JsonResponse({"estado": "error", "msg": "No fue posible registrar asistencia"}, status=400)
        
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno"},status=500)


class PagoEmpleado(APIView):
    @logueado()
    def post(self, request, id):

        admin_id = get_admin_id_from_request(request)

        try:
            pago_empleado(admin_id, id, data=request.data)

            return JsonResponse({"estado":"ok", "msg":"Pago realizado"}, status=HTTPStatus.OK)
        except Exception:
              return JsonResponse({"estado": "error", "msg": "No fue posible realizar el pago"}, status=400)
        
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno"},status=500)