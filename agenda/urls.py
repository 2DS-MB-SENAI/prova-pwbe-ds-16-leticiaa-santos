from django.urls import path
from . import views

urlpatterns = [
    path('servicos/', view=views.servicos, name='servicos'),
    path('servicos/<int:pk>/', view=views.servico_especifico, name='servico_especifico'),
]