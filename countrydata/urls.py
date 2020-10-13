from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('confirm/<int:uid>', views.confirmation_email, name='confirmation'),
    path('updates/', views.update_emails, name="updates")
]