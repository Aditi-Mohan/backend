from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .functions import verify, send_email_to_sub, update_date
from .models import Data, initialize, Subscriber, Messages
from .serializers import DataSerializer, SubscriberSerializer, MessagesSerializer
import pandas as pd
from rest_framework.response import Response


def index(request):
    update_date()
    # initialize()
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
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

class MessagesView(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer