from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pacientes, name='lista_pacientes'),
    path('paciente/<int:pk>/', views.pacientes_detail, name='pacientes_detail'),
    path('paciente/new/', views.paciente_new, name='paciente_new'),
    path('paciente/<int:pk>/edit/', views.pacientes_edit, name='pacientes_edit'),
    ]
