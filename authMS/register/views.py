from rest_framework.views import APIView
from django.http.response import JsonResponse
from django.http import Http404
from http import HTTPStatus
from django.contrib.auth.models import User
import uuid
from django.contrib.auth import authenticate
from jose import jwt
from django.conf import settings
from datetime import datetime, timedelta
import time
import os
from dotenv import load_dotenv
from .models import *
from utils import utils

# Create your views here.

class Clasel(APIView):

    def post(self, request):

        #Validaciones generales
        if request.data.get("email") == None or not request.data.get("email"):
            return JsonResponse({"estado": "error", "msg":"El campo correo es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("nombre") == None or not request.data.get("nombre"):
            return JsonResponse({"estado": "error", "msg":"El campo nombre es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("password") == None or not request.data.get("password"):
            return JsonResponse({"estado": "error", "msg":"El campo contraseña es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        
        #Validación usuario unico
        if User.objects.filter(email=request.data["email"]).exists():
            return JsonResponse({"estado":"error", "msg":"El correo ya se encuentra registrado"}, status=HTTPStatus.BAD_REQUEST)
        
        token = uuid.uuid4()
        url = os.getenv("BASE_URL")+"api/v1/auth/confirmar-cuenta/"+str(token)
       

        try:
           
            u=User.objects.create_user(username=request.data["nombre"], 
                                        password=request.data["password"], 
                                        email=request.data["email"], 
                                        first_name=request.data["nombre"], 
                                        last_name="", 
                                        is_active=0)
            
            UserMetaData.objects.create(token=token, user_id=u.id)
            
            
            html=f"""
                    Hola {request.data["nombre"]}, para confirmar tu cuenta accede al siguiente enlace
                    <a href="{url}">aqui</a>
                    o copia y pega el siguiente enlace en tu navegador: {url}
                    """

            utils.sendEmail(html, "Verificacion", request.data["email"])


            return JsonResponse({"estado":"ok", "msg":"Registro exitoso"}, status=HTTPStatus.OK)
        
        except Exception as e:
            return JsonResponse({"estado":"error", "msg":"Ha ocurrido un problema"}, status=HTTPStatus.BAD_REQUEST)


class Clasell(APIView):

    def post(selft, request, token):


        #Confirmamos que exista el token
        if token == None or not token:
            return JsonResponse({"estado":"error", "msg":"La cuenta ya fue validada"}, status=Http404)

        try:
            data= UserMetaData.objects.filter(token=token).filter(user__is_active=0).get()

            UserMetaData.objects.filter(token=token).update(token="")

            User.objects.filter(id=data.user_id).update(is_active=1)

            return JsonResponse({"estado":"ok", "msg":"Cuenta verificada correctamente"}, status=HTTPStatus.OK)
        
        except UserMetaData.DoesNotExist:
            raise Http404


