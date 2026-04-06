from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import Proveedor

class ProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proveedor
        fields = ("id", "admin_id", "nombre_completo", "telefono", "email", "rut", 
                  "nombre_empresa", "direccion", "is_active", "observaciones", "created_at")

class ObtenerProveedoresSerializer(serializers.Serializer):

    admin_id = serializers.CharField(
        required=True,
        allow_blank=False,
    )

    id = serializers.CharField(required=False, allow_blank=True)
    nombre_completo = serializers.CharField(required=False, allow_blank=True)
    telefono = serializers.CharField(required=False, allow_blank=True)          
    email = serializers.EmailField(required=False, allow_blank=True)
    rut = serializers.CharField(required=False, allow_blank=True)
    nombre_empresa = serializers.CharField(required=False, allow_blank=True)
    direccion = serializers.CharField(required=False, allow_blank=True)
    is_active = serializers.BooleanField(required=False)
    observaciones = serializers.CharField(required=False, allow_blank=True)
    
    class Meta:
        model = Proveedor
        fields = ("id", "admin_id", "nombre_completo", "telefono", "email", "rut", 
                  "nombre_empresa", "direccion", "is_active", "observaciones", "created_at")

class NewProveedorSerializer(serializers.Serializer):
    
    nombre_completo = serializers.CharField(
        required=False,
        allow_blank=False,
        error_messages={ 'required': 'El nombre del Representante es requerido.',
            'blank': 'El nombre del Representante no puede estar vacío.',
        },
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 ]+$',
                message="El nombre solo puede contener letras, números y espacios."
            )
        ]
    )

    telefono = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=20,
        error_messages={
            'required': 'El teléfono es obligatorio.',
            'blank': 'El teléfono no puede estar vacío.',
        },
        validators=[
            RegexValidator(
                regex=r'^\+?\d{7,15}$',
                message="El número de teléfono debe contener entre 7 y 15 dígitos, y puede incluir un prefijo '+'"
            )
        ]
    )

    email = serializers.EmailField(
        required=False,
        allow_blank=True,
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^[\w\.-]+@[\w\.-]+\.\w+$',
                message="Ingrese un correo electrónico válido."
            )
        ])
    
    rut = serializers.CharField(
        required=False,     
        allow_blank=True,
        max_length=12,
       )
    
    nombre_empresa = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=100,
        error_messages={
            'required': 'El nombre de la empresa es requerido.',
            'blank': 'El nombre de la empresa no puede estar vacío.',
        },
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 ]+$',
                message="El nombre solo puede contener letras, números y espacios."
            )
        ]
    )

    direccion = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 ]+$',
                message="El nombre solo puede contener letras, números y espacios."
            )
        ]
    )

    observaciones = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 ]+$',
                message="El nombre solo puede contener letras, números y espacios."
            )
        ]
    )

    is_active = serializers.BooleanField(required=False, allow_null=False)

    def validate_rut(self, value):
        admin_id = self.context.get("admin_id")
        if value is not None and value != "":
            if Proveedor.objects.filter( rut=value, admin_id=admin_id).exists():
                #admin_id=admin_id,
                raise serializers.ValidationError("El rut ingresado ya existe.")
            return value

    def validate_telefono(self, value):
        admin_id = self.context.get("admin_id")
        if value is not None and value != "":
            if Proveedor.objects.filter(admin_id=admin_id, telefono=value).exists():
                raise serializers.ValidationError("El telefono ingresado ya existe.")
            return value
    
    def validate_email(self, value):
        admin_id = self.context.get("admin_id")
        if value is not None and value != "":
            if Proveedor.objects.filter(admin_id=admin_id, email=value).exists():
                raise serializers.ValidationError("El correo electrónico ingresado ya existe.")
            return value

class EditProveedorSerializer(serializers.Serializer):
    nombre_completo = serializers.CharField(
        required=False,
        allow_blank=False,
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 ]+$',
                message="El nombre solo puede contener letras, números y espacios."
            )
        ]
    )

    telefono = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?\d{7,15}$',
                message="El número de teléfono debe contener entre 7 y 15 dígitos, y puede incluir un prefijo '+'"
            )
        ]
    )

    email = serializers.EmailField(
        required=False,
        allow_blank=True,
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^[\w\.-]+@[\w\.-]+\.\w+$',
                message="Ingrese un correo electrónico válido."
            )
        ])
    
    rut = serializers.CharField(
        required=False,     
        allow_blank=True,
        max_length=12,
       )
    
    nombre_empresa = serializers.CharField(
        required=False,
        allow_blank=False,
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 ]+$',
                message="El nombre solo puede contener letras, números y espacios."
            )
        ]
    )

    direccion = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 ]+$',
                message="El nombre solo puede contener letras, números y espacios."
            )
        ]
    )

    observaciones = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 ]+$',
                message="El nombre solo puede contener letras, números y espacios."
            )
        ]
    )

    is_active = serializers.BooleanField(required=False, allow_null=False)

    def validate_rut(self, value):
        admin_id = self.context.get("admin_id")
        if Proveedor.objects.filter( rut=value, admin_id=admin_id).exists():
            #admin_id=admin_id,
            raise serializers.ValidationError("El rut ingresado ya existe.")
        return value

    def validate_telefono(self, value):
        admin_id = self.context.get("admin_id")
        print(admin_id)
        if Proveedor.objects.filter(admin_id=admin_id, telefono=value).exists():
            raise serializers.ValidationError("El telefono ingresado ya existe.")
        return value
    
    def validate_email(self, value):
        admin_id = self.context.get("admin_id")
        print(admin_id)
        if Proveedor.objects.filter(admin_id=admin_id, email=value).exists():
            raise serializers.ValidationError("El correo electrónico ingresado ya existe.")
        return value
    
class ProveedoresListBoxSerializer(serializers.Serializer):

    admin_id = serializers.CharField(
        required=True,
        allow_blank=False,
    )

    id = serializers.CharField(required=False, allow_blank=True)
    nombre_empresa = serializers.CharField(required=False, allow_blank=True)
    nombre_completo = serializers.CharField(required=False, allow_blank=True)
    is_active = serializers.BooleanField(required=False)
    telefono = serializers.CharField(required=False, allow_blank=True)          
    email = serializers.EmailField(required=False, allow_blank=True)

    class Meta:
        model = Proveedor
        fields = ("id", "admin_id", "nombre_completo", "nombre_empresa", "is_active", "telefono", "email")