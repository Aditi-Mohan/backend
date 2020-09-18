from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('<str:name>', views.get_name, name='ind_country')
]