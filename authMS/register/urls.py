from django.urls import path
from .views import*

urlpatterns = [
    path('registro', Clasel.as_view()),
    path('confirmar-cuenta/<str:token>', Clasell.as_view()),
    path('login', Claselll.as_view()),
    path('recuperar-password', ClaseIV.as_view()),
    path('cambiar-password/<str:token>', ClaseV.as_view())
]
