from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pacientes, name='lista_pacientes'),
    path('paciente/<int:pk>/', views.paciente_detail, name='paciente_detail'),
    path('', views.lista_clinicos, name='lista_clinicos'),
    path('clinico/<int:pk>/', views.clinico_detail, name='clinico_detail'),
    path('', views.lista_secretarios, name='lista_secretarios'),
    path('secretario/<int:pk>/', views.secretario_detail, name='secretario_detail'),

]
