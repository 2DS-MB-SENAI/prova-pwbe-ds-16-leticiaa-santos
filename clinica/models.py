from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=5)
    escolha_especialidade = (
        ('Pediatra', 'Pediatra'),
        ('Clinico', 'Clinico'),
        ('Oftalmologista', 'Oftalmologista'),
        ('CAR', 'Cardiologista'),
        ('Ortopedista', 'Ortopedista')
    )
    especialidade = models.CharField(max_length=20, choices=escolha_especialidade, blank=True)
    crm = models.CharField(max_length=8, unique=True)
    email = models.EmailField(blank=True, null=True)

    REQUIRED_FIELDS = ['nome', 'especialidade', 'crm', 'email']

    def __str__(self):
        return self.nome
    

class Consulta(models.Model):
    paciente = models.CharField(max_length=50)
    data = models.DateField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    escolha_status = (
        ('agendado', 'agendado'),
        ('realizado', 'realizado'),
        ('cancelado', 'cancelado')
    )

    def __str__(self):
        return self.paciente
