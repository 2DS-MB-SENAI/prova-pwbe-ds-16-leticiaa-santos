from django.urls import path
from . import views

urlpatterns = [
    path('servicos/', view=views.servicos, name='servicos'),
    path('servicos/<int:pk>/', view=views.servico_especifico, name='servico_especifico'),
    path('agendamentos/', view=views.agendamentos, name='agendamentos'),
    path('agendamentos/<int:pk>/', view=views.agendamento_especifico, name='agendamento_especifico'),
]