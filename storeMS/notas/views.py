from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus

#Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

#Locales
from .utils.auth import get_admin_id_from_request
from services import*
from decorators.decorators import logueado
from serializers import*

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