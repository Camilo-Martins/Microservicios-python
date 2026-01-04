from django.urls import path
from .views import*

urlpatterns = [
    path('registro-empleado', Clasel.as_view()),
    path('obtener-empleados', Clasel.as_view()),
    path('obtener-empleado/<int:id>', Clasel.as_view()),
    path('editar-empleado/<int:id>', Clasel.as_view()),
    path('desactivar-empleado/<int:id>', Clasel.as_view())
]
