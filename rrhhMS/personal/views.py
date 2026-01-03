from django.shortcuts import render

from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404
from .models.empleado import*
from django.utils.dateformat import DateFormat
from dotenv import load_dotenv
import os
from datetime import datetime

from decorators.decorators import logueado
# Create your views here.

class Clasel(APIView):

    @logueado()
    def get(self, request):
        return JsonResponse({"data":{"ok":"next"}})