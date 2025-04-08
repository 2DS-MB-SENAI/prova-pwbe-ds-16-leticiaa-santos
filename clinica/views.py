from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico, Consulta
from .forms import ConsultaForm

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

def detalhes_consulta(request, pk):
    consultas = get_object_or_404(Consulta, pk=pk)
    return render(request, 'clinica/form_consulta.html', {'consultas' : consultas})

def criar_consulta(request):
    if request == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detalhes_consulta')
    else:
        form = ConsultaForm()
    return render(request, 'clinica/form_consulta.html', {'form' : form})