from django.urls import path
from .views import*

urlpatterns = [
    path('agregar', AgregarProducto.as_view()),
    path('obtener/', ObtenerProductos.as_view()),
    path('editar/<int:id>', EditarProducto.as_view())
]
