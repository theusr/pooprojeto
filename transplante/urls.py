from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('paciente/lista_pacientes', views.lista_pacientes, name='lista_pacientes'),
    path('paciente/<int:pk>/', views.pacientes_detail, name='pacientes_detail'),
    path('paciente/new/', views.paciente_new, name='paciente_new'),
    path('paciente/<int:pk>/edit/', views.pacientes_edit, name='pacientes_edit'),
    path('clinico/lista_clinicos', views.lista_clinicos, name='lista_clinicos'),
    path('clinico/<int:pk>/', views.clinicos_detail, name='clinicos_detail'),
    path('clinico/new/', views.clinico_new, name='clinico_new'),
    path('clinico/<int:pk>/edit/', views.clinicos_edit, name='clinicos_edit'),
    path('secretario/lista_secretarios', views.lista_secretarios, name='lista_secretarios'),
    path('secretario/<int:pk>/', views.secretarios_detail, name='secretarios_detail'),
    path('secretario/new/', views.secretario_new, name='secretario_new'),
    path('secretario/<int:pk>/edit/', views.secretarios_edit, name='secretarios_edit'),
    ]
