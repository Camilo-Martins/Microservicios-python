from personal.models import Empleado
from horarios.models import AsignacionDia, DiaHorario

def asignar_empleado_a_dia(admin_id, dia, empleado_id):

    try:
        empleado = Empleado.objects.get(
            id=empleado_id,
            admin_id=admin_id,
            is_active=True
        )
    except Empleado.DoesNotExist:
        return "Empleado no válido"

    # máximo 2 empleados por día
    if AsignacionDia.objects.filter(dia=dia).count() >= 2:
        return "Máximo de empleados alcanzado para este día"

    # no repetir empleado
    if AsignacionDia.objects.filter(dia=dia, empleado=empleado).exists():
        return "Empleado ya asignado a este día"

    AsignacionDia.objects.create(
        dia=dia,
        empleado=empleado
    )

    return None
