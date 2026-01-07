from django.urls import path
from .views import*

urlpatterns = [
    path('registro-empleado', RegistroEmpleado.as_view()),
    path('obtener-empleados', ObtenerEmpleados.as_view()),
    path('obtener-empleado/<int:id>', ObtenerEmpleado.as_view()),
    path('desactivar-empleado/<int:id>', DesactivarEmpleado.as_view()),
    path('editar-empleado/<int:id>', EditarEmpleado.as_view()),
    path('asistencia-empleado/<int:id>', AsistenciaEmpleado.as_view()),
    path('pago-empleado/<int:id>', PagoEmpleado.as_view())
]
