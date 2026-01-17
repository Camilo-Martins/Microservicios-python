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
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Ha ocurrido un error"}, status=500)

        serializer = GetPersonalListSerializer(data={"admin_id":admin_id})
        serializer.is_valid(raise_exception=True)

        personalList = PersonalListService.obtener_empleados_por_admin(
            **serializer.validated_data
        )

        datos_json = EmpleadoSerializer(personalList, many=True)

        return JsonResponse({"data": datos_json.data})


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
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno del servidor"},status=500)
        
        
        serializer = GetPersonalSerializer(data={"admin_id":admin_id, "id":id})
        serializer.is_valid(raise_exception=True)

        empleado, asistencias, pagos = PersonalService.obtener_empleado(
            admin_id=admin_id,
            id=id
        )

        data = {
            "empleado": EmpleadoSerializer(empleado).data,
            "asistencias": AsistenciaSerializer(asistencias, many=True).data,
            "pagos": PagoSerializer(pagos, many=True).data,
        }
        
        return JsonResponse(data)
      
       
        
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
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno"},status=500)
        
        serializer = NewPersonalSerializer(admin_id, request.data)
        serializer.is_valid(raise_exception=True)

        NewPersonalService.crear_empleado(
            admin_id=admin_id,
            **serializer.validated_data
        )

        return JsonResponse(
                {"estado": "ok", "msg": "Registro exitoso"},
                status=201
            )


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
        
        try:
            admin_id = get_admin_id_from_request(request)
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno"},status=500)
       
        serializer = SetPersonalSerializer(data={"admin_id":admin_id, "id":id})
        serializer.is_valid(raise_exception=True)
    
        SetPerfilService.desactivar_empleado(
            **serializer.validated_data
        )

        return JsonResponse( {"estado": "ok", "msg": "Estado actualizado"},status=200)

        
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
        try:
            admin_id = get_admin_id_from_request(request)
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno"},status=HTTPStatus.INTERNAL_SERVER_ERROR)
       

        serializer = EditPersonalSerializer(
            data=request.data,
            context={
                "admin_id": admin_id,
                "id": id
            }
        )
        serializer.is_valid(raise_exception=True)
        
        
        EditPersonalService.editar_empleado(
            admin_id=admin_id,
            id=id,
            **serializer.validated_data
        )

        return JsonResponse( {"estado": "ok", "msg": "Estado actualizado"},status=200)
      
        

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