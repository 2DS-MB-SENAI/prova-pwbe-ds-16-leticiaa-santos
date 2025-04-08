from django.shortcuts import render
from .models import Medico, Consulta

def listar_medicos(request):
    if request.method == 'POST':
        medico = espc_filter(request)
    else:
        medico = []
    medicos = Medico.objects.all()
    return render(request, 'clinica/listar_medicos.html', {'medicos' : medicos, 'medico' : medico})

def espc_filter(request):
    filtro = request.POST.get('espc_filter')
    medico = Medico.objects.filter(especialidade__icontains = filtro)
    return medico