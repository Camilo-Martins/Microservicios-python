from django.urls import path
from .views import*

urlpatterns = [
    path('registro', Clasel.as_view()),
    path('confirmar-cuenta/<str:token>', Clasell.as_view())
]
