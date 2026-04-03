from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from datetime import timedelta
from django.db import transaction
from .models import*

class NotasService:
    @staticmethod
    @transaction.atomic

    def obtener_notas_por_admin(*, admin_id):
        notasList = Nota.objects.filter(admin_id=admin_id)
        return notasList
    

class NewNotaService:
    @staticmethod
    @transaction.atomic
    def crear_nota(*,admin_id, nombre_nota, observaciones):

        nota = Nota.objects.create(
            nombre_nota=nombre_nota,
            observaciones=observaciones,
            is_active=True,
            admin_id=admin_id
        )

        return nota
    
class EditNotaService:
    @staticmethod
    @transaction.atomic
    def editar_nota(*, admin_id, id, nombre_nota, observaciones, is_active):
        
        nota = get_object_or_404(
            Nota,
            admin_id=admin_id,
            id=id
        )

        nota.nombre_nota = nombre_nota
        nota.observaciones = observaciones
        nota.is_active = is_active
        nota.save(update_fields=["nombre_nota", "observaciones", "is_active"])
        
        return nota