from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pacientes, name='lista_pacientes'),
    path('paciente/<int:pk>/', views.paciente_detail, name='paciente_detail'),
    ]
