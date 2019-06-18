from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    
    path('paciente/lista_pacientes', views.lista_pacientes, name='lista_pacientes'),
    path('paciente/<int:pk>/', views.pacientes_detail, name='pacientes_detail'),
    path('paciente/new/', views.paciente_new, name='paciente_new'),
    path('paciente/<int:pk>/edit/', views.pacientes_edit, name='pacientes_edit'),
    path('paciente/<int:pk>/remover/', views.remove_paciente, name='remove_paciente'),
    
    path('clinico/lista_clinicos', views.lista_clinicos, name='lista_clinicos'),
    path('clinico/<int:pk>/', views.clinicos_detail, name='clinicos_detail'),
    path('clinico/new/', views.clinico_new, name='clinico_new'),
    path('clinico/<int:pk>/edit/', views.clinicos_edit, name='clinicos_edit'),
    path('clinico/<int:pk>/remover/', views.remove_clinico, name='remove_clinico'),
    
    path('secretario/lista_secretarios', views.lista_secretarios, name='lista_secretarios'),
    path('secretario/<int:pk>/', views.secretarios_detail, name='secretarios_detail'),
    path('secretario/new/', views.secretario_new, name='secretario_new'),
    path('secretario/<int:pk>/edit/', views.secretarios_edit, name='secretarios_edit'),
    path('secretario/<int:pk>/remover/', views.remove_secretario, name='remove_secretario'),

    path('cirurgia/lista_cirurgias', views.lista_cirurgias, name='lista_cirurgias'),
    path('cirurgia/<int:pk>/', views.cirurgias_detail, name='cirurgias_detail'),
    path('cirurgia/new/', views.cirurgia_new, name='cirurgia_new'),
    path('cirurgia/<int:pk>/edit/', views.cirurgias_edit, name='cirurgias_edit'),
    path('cirurgia/<int:pk>/remover/', views.remove_cirurgia, name='remove_cirurgia'),
    ]
