from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Confirmed, Death, Recovery, initialise_table
from .serializers import ConfirmedSerializer, DeathSerializer, RecoverySerializer


def index(request):
    initialise_table('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv', 'confirmed')
    initialise_table('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv', 'death')
    initialise_table('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv', 'recovery')
    return HttpResponse('success')

class ConfirmedView(viewsets.ModelViewSet):
    serializer_class = ConfirmedSerializer
    queryset = Confirmed.objects.all()

class DeathView(viewsets.ModelViewSet):
    serializer_class = DeathSerializer
    queryset = Death.objects.all()

class RecoveryView(viewsets.ModelViewSet):
    serializer_class = RecoverySerializer
    queryset = Recovery.objects.all()
