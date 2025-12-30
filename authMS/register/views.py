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
        print(url)

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
            return JsonResponse({"estado":"error", "msg": "Error."}, status=HTTPStatus.BAD_REQUEST)



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


class Claselll(APIView):

    def post(self,request):
       
        if request.data.get("email") == None or not request.data.get("email"):
            return JsonResponse({"estado": "error", "msg":"El campo correo es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("password") == None or not request.data.get("password"):
            return JsonResponse({"estado": "error", "msg":"El campo contraseña es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
    
        try:
            user = User.objects.filter(email=request.data["email"]).get()
           

        except User.DoesNotExist:
            return JsonResponse({"estado":"error", "mensaje": "Hubo un problema"}, status=HTTPStatus.BAD_REQUEST)

     
        auth = authenticate(request, username=user.username, password=request.data.get("password"))    
        
    
        if auth is not None:
          
            fecha = datetime.now()
            despues = fecha + timedelta(days=1)
            fecha_numero = int(datetime.timestamp(despues))

            payload={
                "id": user.id,
                "IIS": os.getenv("BASE_URL"),
                "iat": int(time.time()),
                "exp": int(fecha_numero)
            }

            try:
                token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS512')
                return JsonResponse({"id": user.id, "nombre": user.first_name, "token": token})

            except Exception as e:
                return JsonResponse({"estado":"error", "mensaje": "No es posible ingresar"}, status=404)
        else:
            return JsonResponse({"estado":"error", "mensaje": "Problemas al ingresar"}, status=404)
        


class ClaseIV(APIView):

    def post(self,request):
            
        if request.data.get("email") == None or not request.data.get("email"):
            return JsonResponse({"estado": "error", "msg":"El campo correo es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        
        token = uuid.uuid4()
        url = os.getenv("BASE_URL")+"api/v1/auth/resetear-password/"+str(token)
        print(url)

        try:
            user = User.objects.filter(email=request.data["email"]).get()
            UserMetaData.objects.filter(user_id=user.id).update(token=token)
        

            html=f"""
                Hola {user.username}, para cambiar tu contraseña
               <a href="{url}">aqui</a>
                o copia y pega el siguiente enlace en tu navegador: {url}
                """

            utils.sendEmail(html, "Verificacion", request.data["email"])

         

            return JsonResponse({"estado":"correo enviado", "mensaje": "OK"}, status=HTTPStatus.OK)
        except Exception as e :
            return JsonResponse({"estado":"error", "mensaje": "No es posible ingresar"}, status=HTTPStatus.BAD_REQUEST)
        

class ClaseV(APIView):

    def post(self,request,token):
            
        if request.data.get("password") == None or not request.data.get("password"):
            return JsonResponse({"estado": "error", "msg":"Debe agregar una contraseña!"}, status=HTTPStatus.BAD_REQUEST)
        
        if token == None or not token:
            return JsonResponse({"estado":"error", "msg":"La cuenta ya fue validada"}, status=Http404)

        try:
            data = UserMetaData.objects.filter(token=token).get()

            UserMetaData.objects.filter(token=token).update(token="")

          
            user = User.objects.filter(id=data.user_id)
            user.set_password(request.data.get("password"))
            user.save()

            html=f"""
                Hola {user.username}, tu contraseña ha sido actualizada
             
                """

            utils.sendEmail(html, "Verificacion", user.email)

            return JsonResponse({"estado":"correo enviado", "mensaje": "OK"}, status=HTTPStatus.OK)
        except Exception as e :
            return JsonResponse({"estado":"error", "mensaje": "No es posible ingresar"}, status=HTTPStatus.BAD_REQUEST)
