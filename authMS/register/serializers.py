from rest_framework import serializers
from django.db import transaction
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.validators import RegexValidator

from .models import UserStore

User = get_user_model()

class RegisterStoreSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 ]+$',
                message="El nombre solo puede contener letras, números y espacios."
            )
        ]
    )
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)
    nombre_tienda = serializers.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 ]+$',
                message="El nombre de la tienda solo puede contener letras, números y espacios."
            )
        ]
    )

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Usuario ya existente.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este correo ya está registrado.")
        return value

    def validate_store_name(self, value):
        if UserStore.objects.filter(nombre_tienda=value).exists():
            raise serializers.ValidationError("El nombre de la tienda ya existe.")
        return value

    def validate_password(self, value):
        try:
            validate_password(value)
        except DjangoValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value    


class ConfirmAccountSerializer(serializers.Serializer):

    token = serializers.CharField()

    def validate_token(self,value):

        if value == None or not value:
            raise serializers.ValidationError("Error al activar cuenta")

        if not UserStore.objects.filter(token=value).exists():
            raise serializers.ValidationError("Error al activar cuenta")

        return value
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


    def validate_email(self,value):
        if value == None or not value:
            raise serializers.ValidationError("Ingrese correo")
        
        return value
    
    def validate_password(self,value):
        if value == None or not value:
            raise serializers.ValidationError("Ingrese contraseña")
    
        return value
    
class ResetPassSerielizer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self,value):
        if value == None or not value:
            raise serializers.ValidationError("Ingrese correo")
        
        return value
     

class NewPassSerielizer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField()

    def validate_token(self,value):

        if value == None or not value:
            raise serializers.ValidationError("Token expirado")

        if not UserStore.objects.filter(token=value).exists():
            raise serializers.ValidationError("Token expirado")

        return value

    def validate_password(self,value):
        if value == None or not value:
            raise serializers.ValidationError("Ingrese contraseña")
        
        return value