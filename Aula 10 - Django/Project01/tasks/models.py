from django.db import models
from phone_field import PhoneField


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
        db_table = 'task'

class Agenda(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.nome
