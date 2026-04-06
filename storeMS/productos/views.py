from rest_framework.views import APIView
from django.shortcuts import render
from django.http.response import JsonResponse

#Locales
from .utils.auth import get_admin_id_from_request
from .services import*
from decorators.decorators import logueado
from .serializers import*
from django.shortcuts import render

# Create your views here.
class ObtenerProductos(APIView):

    @logueado()
    def get(self, request):
        try:
            admin_id = get_admin_id_from_request(request)
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Ha ocurrido un error"}, status=500)
        
        proveedor = request.query_params.get('proveedor')
        categoria = request.query_params.get('categoria')

        serializer = ProductoSerializer(data={"admin_id":admin_id})
        serializer.is_valid(raise_exception=True)
        
        productosList = ProductoService.get_productos(
            **serializer.validated_data,
            proveedor=proveedor,
            categoria=categoria
        )

        datos_json = ProductoSerializer(productosList, many=True)

        return JsonResponse({"data": datos_json.data})

class AgregarProducto(APIView):
    @logueado()

    def post(self, request):

        try:
            admin_id = get_admin_id_from_request(request)
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Ha ocurrido un error"}, status=500)

        serializer = NewProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        producto = NewProductoService.crear_producto(
            **serializer.validated_data,
            admin_id=admin_id
        )

        datos_json = ProductoSerializer(producto)

        return JsonResponse({"data": datos_json.data})
    
class EditarProducto(APIView):
    @logueado()

    def put(self, request, id):

        try:
            admin_id = get_admin_id_from_request(request)
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Ha ocurrido un error"}, status=500)

        serializer = EditarProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        producto = EditProductoService.editar_producto(
            **serializer.validated_data,
            admin_id=admin_id,
            id=id
        )

        datos_json = EditarProductoSerializer(producto)

        return JsonResponse({"data": datos_json.data})