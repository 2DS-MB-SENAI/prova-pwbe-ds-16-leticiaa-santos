from django.urls import path
from . import views

urlpatterns = [
    path('medicos/', views.listar_medicos, name='listar_medico'),
    path('consultas/nova/', views.criar_consulta, name='criar_consulta'),
    path('consultas/', views.detalhes_consulta, name='detalhes_consulta'),
]