from rest_framework.views import APIView
from django.shortcuts import render
from django.http.response import JsonResponse

#Locales
from .utils.auth import get_admin_id_from_request
from .services import*
from decorators.decorators import logueado
from .serializers import*

# Create your views here.

class ObtenerProveedores(APIView):
    @logueado()
 
    def get(self, request):
        try:
            admin_id = get_admin_id_from_request(request)
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Ha ocurrido un error"}, status=500)
        
        serializer = ObtenerProveedoresSerializer(data={"admin_id":admin_id})
        serializer.is_valid(raise_exception=True)

        proveedoresLists = ProveedoresService.obtener_proveedores_por_admin(
            **serializer.validated_data
        )

        datos_json = ObtenerProveedoresSerializer(proveedoresLists, many=True)

        return JsonResponse({"data": datos_json.data})


class ObtenerProveedoresListBox(APIView):
    @logueado()
 
    def get(self, request):
        try:
            admin_id = get_admin_id_from_request(request)
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Ha ocurrido un error"}, status=500)
        
        serializer = ProveedoresListBoxSerializer(data={"admin_id":admin_id})
        serializer.is_valid(raise_exception=True)

        proveedoresLists = ProveedoresService.obtener_proveedores_por_admin_cbox(
            **serializer.validated_data
        )

        datos_json = ProveedoresListBoxSerializer(proveedoresLists, many=True)

        return JsonResponse({"data": datos_json.data})

class AgregarProveedor(APIView):
    @logueado()

    def post(self, request):

        try:
            admin_id = get_admin_id_from_request(request)
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno"},status=500)
        
        serializer = NewProveedorSerializer(context={"admin_id": admin_id}, data=request.data)
        serializer.is_valid(raise_exception=True)

        NewProveedorService.crear_proveedor(  admin_id=admin_id,
            **serializer.validated_data
        )

        return JsonResponse({"estado": "ok", "msg": "Registro exitoso"},status=201)
    
class EditarProveedor(APIView):
    @logueado()

    def put(self, request, id):

        try:
            admin_id = get_admin_id_from_request(request)
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno"},status=500)

        serializer = EditProveedorSerializer(context={"admin_id": admin_id}, data=request.data)
        serializer.is_valid(raise_exception=True)

        EditProveedorService.editar_proveedor(  admin_id=admin_id,
            id=id,
            **serializer.validated_data
        )

        return JsonResponse({"estado": "ok", "msg": "Edición exitosa"},status=200)