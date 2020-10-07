from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Data, initialize
from .serializers import DataSerializer
import pandas as pd


def index(request):
    initialize()
    return HttpResponse('success')

class DataView(viewsets.ModelViewSet):
    serializer_class = DataSerializer
    queryset = Data.objects.all()

class Top5View(viewsets.ModelViewSet):
    serializer_class = DataSerializer
    queryset = Data.objects.all()[:5]