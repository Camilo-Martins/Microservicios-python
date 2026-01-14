from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
import uuid
import os
from datetime import timedelta, datetime
import time

from ..models import *
from ..utils import send_email, get_token, regex
from django.db import transaction

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