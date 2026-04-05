from django.urls import path
from .views import*

urlpatterns = [
    path('agregar', AgregarProveedor.as_view()),
    path('obtener', ObtenerProveedores.as_view()),
    path('obtener/lista', ObtenerProveedoresListBox.as_view()),
    path('editar/<int:id>', EditarProveedor.as_view())
]
