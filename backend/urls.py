"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from countrydata import views
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'data', views.DataView, 'dataview')
router.register(r'top5', views.Top5View, 'top5view')
router.register(r'subscriber', views.SubscriberView, 'subscriberview')
router.register(r'messages', views.MessagesView, 'messagesview')

urlpatterns = [
    path('countrydata/', include("countrydata.urls"), name='countrydata'),
    path('api/', include(router.urls)),
    path('email_verification/<str:email>', views.verify_email)
]
