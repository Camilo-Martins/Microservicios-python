from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
import uuid
import os
from datetime import timedelta, datetime
import time

from ..models import *
from ..utils import send_email, get_token, regex
from django.db import transaction


User = get_user_model()

print(User)
print(User._meta.db_table)

class RegisterService:

    @staticmethod
    @transaction.atomic
    def registro_admin(*, username, email, password, nombre_tienda):

        token = uuid.uuid4()
        url = os.getenv("BASE_URL_FRONTEND") + f"confirmar-cuenta/{token}"

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=username,
            is_active=False
        )

        UserStore.objects.create(
            user=user,
            token=token,
            nombre_tienda=nombre_tienda.lower()
        )

        html = f"""
            Hola {username}, para confirmar tu cuenta accede al siguiente enlace:
            <a href="{url}">aquí</a><br>
            {url}
        """

        send_email.sendEmail(html, "Verificación", email)

        return user
    

class ConfirmService:

    @staticmethod
    @transaction.atomic
    def confirm_account(*, token:str):

        user_store = UserStore.objects.select_for_update().get(token=token)

        User.objects.filter(id=user_store.user_id).update(is_active=True)

        user_store.token = ""
        user_store.save(update_fields=["token"])


class LoginService:
    
    @staticmethod
    @transaction.atomic
    def login(*, email, password):

        email = email.strip().lower()
      
        user = User.objects.filter(email__iexact=email).first()

        if not user:
            raise ValidationError("Credenciales inválidas")

       

        user_meta = UserStore.objects.filter(user_id=user.id).first()
        
        auth = authenticate(
            username=user.username,
            password=password
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

        return  {"id":user.id, 
            "token":token, 
            "nombre":user.first_name, 
            "nombre_tienda":user_meta.nombre_tienda}
    

class ResetPassService:

    @staticmethod
    @transaction.atomic
    def resetPassword(*, email):
        email = email.strip().lower()

        user = User.objects.filter(email__iexact=email).first()

        if not user:
            raise ValidationError("Correo inválido")

        token = uuid.uuid4()
        url = os.getenv("BASE_URL_FRONTEND")+"change-password/"+str(token)

        user_store = UserStore.objects.filter(user=user).update(token=token)
       

        html=f"""
            Hola {user.username}, para cambiar tu contraseña
            <a href="{url}">aqui</a>
            o copia y pega el siguiente enlace en tu navegador: {url}
            """

        send_email.sendEmail(html, "Verificacion", email)


class NewPassService:

    @staticmethod
    @transaction.atomic
    def new_pass(*, token:str, password):

        #Verificamos que exista el token asociado al usario
        meta = get_object_or_404(UserStore, token=token)

        user = User.objects.get(id=meta.user_id)
        user.set_password(password)
        user.save()

        meta.token = ""
        meta.save(update_fields=["token"])

        html = f"""
            Hola {user.username}, tu contraseña ha sido actualizada
        """

        send_email.sendEmail(html, "Verificación", user.email)
