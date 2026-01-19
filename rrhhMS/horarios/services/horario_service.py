from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from datetime import timedelta, date
from django.utils.formats import date_format
from django.core.exceptions import ValidationError
from django.db import transaction
from ..models import*
from helpers.asignaciones import asignar_empleado_a_dia
from ..utils import horario_utils

def obtener_horarios_por_admin(admin_id):
    return HorarioSemanal.objects.filter(admin_id=admin_id).order_by('-id')



class CreateHorarioService:
    @staticmethod
    @transaction.atomic
    def crear_horario(*, admin_id):

        fecha_inicio, fecha_fin, nombre = horario_utils.calcular_semana_actual()
     
        horario_old = HorarioSemanal.objects.filter(admin_id=admin_id).order_by('-id').first()
        
        if horario_old:
            horario_old.is_active = False
            horario_old.save()

        horario = HorarioSemanal.objects.create(
                    nombre=nombre,
                    fecha_inicio=fecha_inicio,
                    fecha_fin=fecha_fin,
                    admin_id=admin_id
                )

        for dia in range(1,8):
            DiaHorario.objects.create(
                horario=horario,
                dia=dia
            )

        return horario

class GetHorarioService:
    @staticmethod
    @transaction.atomic
    def obtener_horario(*, admin_id):

        horario = HorarioSemanal.objects.filter(admin_id=admin_id).order_by('-id').first()
        dias = DiaHorario.objects.filter(horario=horario)

        return horario, dias

def desactivar_horario(admin_id, id):

    horario = get_object_or_404(
        HorarioSemanal,
        admin_id=admin_id,
        id=id
    )

    horario.is_active=True
    horario.save()

        
def asignar_semana(admin_id, id, data):
    asignaciones = data.get("asignaciones")

    if not asignaciones or not isinstance(asignaciones, dict):
        raise ValidationError("Ingrese asignaciones válidas")

    horario = get_object_or_404(
        HorarioSemanal,
        id=id,
        admin_id=admin_id,
        is_active=True
    )

    for dia_num, empleados in asignaciones.items():
        dia = get_object_or_404(
            DiaHorario,
            horario=horario,
            dia=int(dia_num)
        )

        if not isinstance(empleados, list):
            raise ValidationError("Formato de empleados inválido")

        for empleado_id in empleados:
            asignar_empleado_a_dia(
                admin_id=admin_id,
                dia=dia,
                empleado_id=int(empleado_id)
            )