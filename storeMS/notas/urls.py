from django.urls import path
from .views import AgregarNota, ObtenerNotas, EditarNota

urlpatterns = [
    path('agregar', AgregarNota.as_view()),
    path('obtener', ObtenerNotas.as_view()),
    path('editar/<int:id>', EditarNota.as_view())
]
