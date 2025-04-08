from django.urls import path
from . import views

urlpatterns = [
    path('register/', view=views.criar_usuario, name='criar_usuario'),
]