from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from datetime import timedelta

from ..models import*
from horarios.models import*

REQUIRED_FIELDS = [
    "nombre_completo",
    "telefono",
    "rol",
    "pago_diario",
    "rut",
]

# services/empleado_service.py
def obtener_empleados_por_admin(admin_id):
  
    return Empleado.objects.filter(admin_id=admin_id).order_by("id")
   

def obtener_empleado(admin_id,id):
   
    empleado = get_object_or_404(
        Empleado,
        admin_id=admin_id,
        id=id
    )

    asistencias = Asistencia.objects.filter(empleado=empleado)
    pagos = Pago.objects.filter(empleado=empleado)

    return empleado, asistencias, pagos


def crear_empleado(admin_id, data):

    for field in REQUIRED_FIELDS:
        if not data.get(field):
            raise ValidationError(f"El campo {field} es obligatorio")

    if Empleado.objects.filter(telefono=data["telefono"]).exists():
        raise ValidationError("Teléfono ya registrado")

    if Empleado.objects.filter(rut=data["rut"]).exists():
        raise ValidationError("RUT ya registrado")

    return Empleado.objects.create(
        nombre_completo=data["nombre_completo"],
        telefono=data["telefono"],
        rol=data["rol"],
        pago_diario=data["pago_diario"],
        rut=data["rut"],
        medio_pago=data.get("medio_pago"),
        is_active=True,
        admin_id=admin_id
    )

def desactivar_empleado(admin_id,id):
    empleado = get_object_or_404(
    Empleado,
        admin_id=admin_id,
        id=id
    )

    empleado.is_active = not empleado.is_active
    empleado.save(update_fields=["is_active"])

    return empleado.is_active


def editar_empleado(admin_id, id, data):
    
    #Validar que el empleado solo sea editable por el admin
    Empleado.objects.filter(admin_id=admin_id, id=id).get()
    
    for field in REQUIRED_FIELDS:
        if not data.get(field):
            raise ValidationError(f"El campo {field} es obligatorio")
        
    if Empleado.objects.filter(telefono=data["telefono"]).exclude(id=id).exists():
        raise ValidationError("Teléfono ya registrado")

    if Empleado.objects.filter(rut=data["rut"]).exclude(id=id).exists():
        raise ValidationError("RUT ya registrado")

    Empleado.objects.filter(admin_id=admin_id, id=id).update(
        nombre_completo=data["nombre_completo"],
        telefono=data["telefono"],
        rol=data["rol"],
        pago_diario=data["pago_diario"],
        rut=data["rut"],
        medio_pago=data.get("medio_pago"),
        admin_id=admin_id
    )


def asistencia_empleado(admin_id, id, data):

    horario = get_object_or_404(
        HorarioSemanal,
        admin_id=admin_id,
        id=id
    )

    empleado = get_object_or_404(
        Empleado,
        admin_id=admin_id,
        id=data["empleado_id"]
    )

    fecha_asistencia = horario.fecha_inicio + timedelta(days=data["dia"] - 1)

    return Asistencia.objects.create(
        empleado=empleado, 
        asistio = data["asistencia"],
        fecha = fecha_asistencia)


def pago_empleado(admin_id, id, data):

    horario = get_object_or_404(
        HorarioSemanal,
        admin_id=admin_id,
        id=id
    )
    
    fecha_pago = horario.fecha_inicio + timedelta(days=data["dia"] - 1)

    asistencia = get_object_or_404(
        Asistencia,
        id=data["asistencia_id"],
        empleado_id=data["empleado_id"],
        asistio=1
    )
    
    empleado = get_object_or_404(
        Empleado,
        id=data["empleado_id"]
    )

    return Pago.objects.create(
            empleado=empleado, 
            pagado = data["pagado"],
            monto = data["monto"],
            fecha = fecha_pago)