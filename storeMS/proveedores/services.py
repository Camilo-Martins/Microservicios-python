from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from datetime import timedelta
from django.db import transaction
from .models import*

class ProveedoresService:
    @staticmethod
    @transaction.atomic

    def obtener_proveedores_por_admin(*, admin_id):
        proveedoresList = Proveedor.objects.filter(admin_id=admin_id).order_by("-is_active")
        return proveedoresList
    
    def obtener_proveedores_por_admin_cbox(*, admin_id):
        proveedoresList = Proveedor.objects.filter(admin_id=admin_id, is_active=True).order_by("-id")
        return proveedoresList


class NewProveedorService:
    @staticmethod
    @transaction.atomic
    def crear_proveedor(*,admin_id, nombre_completo, telefono=None, email=None, rut=None, nombre_empresa=None, direccion=None, observaciones=None):

        proveedor = Proveedor.objects.create(
            nombre_completo=nombre_completo,
            telefono=telefono,
            email=email,
            rut=rut,
            nombre_empresa=nombre_empresa,
            direccion=direccion,
            observaciones=observaciones,
            is_active=True,
            admin_id=admin_id
        )

        return proveedor
    
class EditProveedorService:
    @staticmethod
    @transaction.atomic
    def editar_proveedor(*, admin_id, id, nombre_completo=None, telefono=None, email=None, rut=None, nombre_empresa=None, direccion=None, observaciones=None, is_active=None):
        
        proveedor = get_object_or_404(
            Proveedor,
            admin_id=admin_id,
            id=id
        )

        proveedor.nombre_completo = nombre_completo if nombre_completo is not None else proveedor.nombre_completo
        proveedor.telefono = telefono if telefono is not None else proveedor.telefono
        proveedor.email = email if email is not None else proveedor.email
        proveedor.rut = rut if rut is not None else proveedor.rut
        proveedor.nombre_empresa = nombre_empresa if nombre_empresa is not None else proveedor.nombre_empresa
        proveedor.direccion = direccion if direccion is not None else proveedor.direccion
        proveedor.observaciones = observaciones if observaciones is not None else proveedor.observaciones
        proveedor.is_active = is_active if is_active is not None else proveedor.is_active 
        proveedor.save(update_fields=["nombre_completo", "telefono", "email", "rut", "nombre_empresa", "direccion", "observaciones", "is_active"])
        
        return proveedor