from functools import wraps
from django.http.response import JsonResponse
from http import HTTPStatus
from jose import jwt
from django.conf import settings
import time
import os
from dotenv import load_dotenv


def logueado():
    def metodo(func):
        @wraps(func)
        def _decorator(request, *args, **kwargs):
            req = args[0]

            if not req.headers.get("Authorization") or req.headers.get("Authorization") == None:
                return JsonResponse({"estado": "error", "mensaje": "Sin Autorización"}, status=HTTPStatus.UNAUTHORIZED)
            
            header= req.headers.get("Authorization").split(" ")

            try:
                resuelto=jwt.decode(header[1], os.getenv("SECRET_KEY"), algorithms=["HS512"])
              
            except Exception as e:
                return JsonResponse({"estado": "error", "mensaje": "Sin Autorización"}, status=HTTPStatus.UNAUTHORIZED)
            
        
            if int(resuelto["exp"])>int(time.time()):
                return func(request, *args, **kwargs)
            else:
                return JsonResponse({"estado": "error", "mensaje": "Sin Autorización"}, status=HTTPStatus.UNAUTHORIZED)

        return _decorator
    return metodo
@logueado()

def post():
    pass