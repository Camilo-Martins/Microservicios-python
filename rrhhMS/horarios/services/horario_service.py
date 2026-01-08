from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from datetime import timedelta, date
from django.utils.formats import date_format
from django.core.exceptions import ValidationError

from ..models import*
from helpers.asignaciones import asignar_empleado_a_dia

def obtener_horarios_por_admin(admin_id):
    return HorarioSemanal.objects.filter(admin_id=admin_id).order_by('-id')

def obtener_horario_por_admin(admin_id,id):
    horario = get_object_or_404(
        HorarioSemanal,
        admin_id=admin_id,
        id=id
    )
    
    dias = DiaHorario.objects.filter(horario=horario)

    return horario, dias

def crear_horario(admin_id, data):
    fecha_inicio = date.today()
    fecha_fin = fecha_inicio + timedelta(days=5)
    
    inicio_str = date_format(fecha_inicio, "d/m/Y")
    fin_str = date_format(fecha_fin, "d/m/Y")

    nombre = f"Horario semana {inicio_str} - {fin_str}"

    if HorarioSemanal.objects.filter(admin_id=admin_id, nombre=nombre, is_active=True).exists():
        raise ValidationError(f"Ya existe un horario asociado a la semana.")
    
    horario = HorarioSemanal.objects.create(
                nombre=nombre,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin,
                admin_id=admin_id
            )

    for dia in range(1,7):
        DiaHorario.objects.create(
            horario=horario,
            dia=dia
        )

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