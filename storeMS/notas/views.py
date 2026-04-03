from rest_framework.views import APIView
from django.http.response import JsonResponse

#Locales
from .utils.auth import get_admin_id_from_request
from .services import*
from decorators.decorators import logueado
from .serializers import*

# Create your views here.

class ObtenerNotas(APIView):
    @logueado()
 
    def get(self, request):
        try:
            admin_id = get_admin_id_from_request(request)
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Ha ocurrido un error"}, status=500)
        
        serializer = ObtenerNotasSerializer(data={"admin_id":admin_id})
        serializer.is_valid(raise_exception=True)

        notasLists = NotasService.obtener_notas_por_admin(
            **serializer.validated_data
        )

        datos_json = ObtenerNotasSerializer(notasLists, many=True)

        return JsonResponse({"data": datos_json.data})
    
class AgregarNota(APIView):
    @logueado()

    def post(self, request):

        try:
            admin_id = get_admin_id_from_request(request)
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno"},status=500)
        
        serializer = NewNotaSerializer(context={"admin_id": admin_id}, data=request.data)
        serializer.is_valid(raise_exception=True)

        NewNotaService.crear_nota(  admin_id=admin_id,
            **serializer.validated_data
        )

        return JsonResponse({"estado": "ok", "msg": "Registro exitoso"},status=201)
    
class EditarNota(APIView):
    @logueado()

    def put(self, request, id):

        try:
            admin_id = get_admin_id_from_request(request)
        except Exception:
            return JsonResponse({"estado": "error", "msg": "Error interno"},status=500)
        
        serializer = EditNotaSerializer(context={"admin_id": admin_id}, data=request.data)
        serializer.is_valid(raise_exception=True)

        EditNotaService.editar_nota(  admin_id=admin_id,
            id=id,
            **serializer.validated_data
        )

        return JsonResponse({"estado": "ok", "msg": "Nota Editada"},status=200)