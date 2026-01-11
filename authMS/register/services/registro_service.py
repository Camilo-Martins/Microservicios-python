from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
import uuid
import os
from datetime import timedelta, datetime
import time
from jose import jwt

from ..models import *
from ..utils import send_email, get_token, regex


REQUIRED_FIELDS = [
    "nombre",
    "email",
    "password",
    "nombre_tienda"
]

def registro_admin(data):

    for field in REQUIRED_FIELDS:
        if not data.get(field):
            raise ValidationError(f"El campo {field} es obligatorio")
        
    if not regex.STORE_NAME_REGEX.match(data["nombre"]):
         raise ValidationError("Nombre")


    if not regex.STORE_NAME_REGEX.match(data["nombre_tienda"]):
         raise ValidationError("Nombre de tienda no disponble")

    #Validación usuario unico
    if User.objects.filter(email=data["email"]).exists():
        raise ValidationError("Correo ya registrado")
    
    if User.objects.filter(username=data["nombre"]).exists():
        raise ValidationError("Correo ya registrado")

    if UserMetaData.objects.filter(nombre_tienda=data["nombre_tienda"]).exists():
        raise ValidationError("Tienda ya registrada")

    


    token = uuid.uuid4()
    url = os.getenv("BASE_URL")+"api/v1/auth/confirmar-cuenta/"+str(token)


    tienda =data["nombre_tienda"].lower()

    u=User.objects.create_user(username=data["nombre"], 
                                password=data["password"], 
                                email=data["email"], 
                                first_name=data["nombre"], 
                                last_name="", 
                                is_active=0)
            
    UserMetaData.objects.create(token=token, user_id=u.id, nombre_tienda=tienda)

    html=f"""
            Hola {data["nombre"]}, para confirmar tu cuenta accede al siguiente enlace
            <a href="{url}">aqui</a>
            o copia y pega el siguiente enlace en tu navegador: {url}
            """

    send_email.sendEmail(html, "Verificacion", data["email"])


def verificar_cuenta(token):
    if token == None or not token:
        raise ValidationError(f"Token expirado")
    
    data= UserMetaData.objects.filter(token=token).filter(user__is_active=0).get()

    UserMetaData.objects.filter(token=token).update(token="")

    User.objects.filter(id=data.user_id).update(is_active=1)


def login_usuario(data):
    for field in ["email", "password"]:
        if not data.get(field):
            raise ValidationError(f"El campo {field} es obligatorio")

    if not regex.STORE_NAME_REGEX.match(data["email"]):
         raise ValidationError("Correo no disponible")

    user = User.objects.get(email=data["email"])
    
    user_meta = UserMetaData.objects.filter(user_id=user.id).first()


    if not user:
        raise ValidationError("Credenciales inválidas")

    auth = authenticate(
        username=user.username,
        password=data["password"]
    )

    if not auth:
        raise ValidationError("Credenciales inválidas")

    exp = int((datetime.now() + timedelta(days=1)).timestamp())

    payload = {
        "id": user.id,
        "iss": os.getenv("BASE_URL"),
        "iat": int(time.time()),
        "exp": exp,
    }

    token = get_token.generateToken(payload)
    nombre = ""
    nombre_tienda = ""

    return  {"id":user.id, 
            "token":token, 
            "nombre":user.first_name, 
            "nombre_tienda":user_meta.nombre_tienda}


def recuperar_password(data):
    if data["email"] == None or not data["email"]:
        raise ValidationError("Ingrese correo")
        
    token = uuid.uuid4()
    url = os.getenv("BASE_URL")+"api/v1/auth/cambiar-password/"+str(token)

    user = User.objects.filter(email=data["email"]).get()
    if not user:
        raise ValidationError("Correo inválido")
    
    UserMetaData.objects.filter(user_id=user.id).update(token=token)

    html=f"""
        Hola {user.username}, para cambiar tu contraseña
        <a href="{url}">aqui</a>
        o copia y pega el siguiente enlace en tu navegador: {url}
        """

    send_email.sendEmail(html, "Verificacion", data["email"])


def cambiar_password(data, token):
    if not data.get("password"):
        raise ValidationError("Ingrese contraseña nueva")

    if not token:
        raise ValidationError("Token inválido o expirado")

    meta = get_object_or_404(UserMetaData, token=token)

    user = User.objects.get(id=meta.user_id)
    user.set_password(data["password"])
    user.save()

    meta.token = ""
    meta.save(update_fields=["token"])

    html = f"""
        Hola {user.username}, tu contraseña ha sido actualizada
    """

    try:
        send_email.sendEmail(html, "Verificación", user.email)
    except Exception:
        pass  # el cambio de password ya fue exitoso