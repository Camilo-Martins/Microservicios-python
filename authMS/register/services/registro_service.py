from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from datetime import timedelta
from django.contrib.auth.models import User
import uuid
import os

from ..models import *
from ..utils import send_email

REQUIRED_FIELDS = [
    "nombre",
    "email",
    "password",
]

def registro_admin(data):

    for field in REQUIRED_FIELDS:
        if not data.get(field):
            raise ValidationError(f"El campo {field} es obligatorio")
        
    #Validación usuario unico
    if User.objects.filter(email=data["email"]).exists():
        raise ValidationError("Correo ya registrado")
    
    token = uuid.uuid4()
    url = os.getenv("BASE_URL")+"api/v1/auth/confirmar-cuenta/"+str(token)

    u=User.objects.create_user(username=data["nombre"], 
                                password=data["password"], 
                                email=data["email"], 
                                first_name=data["nombre"], 
                                last_name="", 
                                is_active=0)
            
    UserMetaData.objects.create(token=token, user_id=u.id)

    html=f"""
            Hola {data["nombre"]}, para confirmar tu cuenta accede al siguiente enlace
            <a href="{url}">aqui</a>
            o copia y pega el siguiente enlace en tu navegador: {url}
            """

    send_email.sendEmail(html, "Verificacion", data["email"])