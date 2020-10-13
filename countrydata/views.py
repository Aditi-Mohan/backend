from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .functions import verify, send_email_to_sub
from .models import Data, initialize, Subscriber
from .serializers import DataSerializer, SubscriberSerializer
import pandas as pd
from rest_framework.response import Response


def index(request):
    initialize()
    return HttpResponse('success')

def verify_email(request, email):
    code = verify(email)
    return JsonResponse({'code': code})

def confirmation_email(request, uid):
    # instead of printing send email
    em = Subscriber.objects.filter(uid=uid)[0]
    return HttpResponse(em.email)

def update_emails(request):
    res = send_email_to_sub()
    return HttpResponse(res)

class DataView(viewsets.ModelViewSet):
    serializer_class = DataSerializer
    queryset = Data.objects.all()

class Top5View(viewsets.ModelViewSet):
    serializer_class = DataSerializer
    queryset = Data.objects.all()[:5]

class SubscriberView(viewsets.ModelViewSet):
    queryset=Subscriber.objects.all()
    serializer_class = SubscriberSerializer
