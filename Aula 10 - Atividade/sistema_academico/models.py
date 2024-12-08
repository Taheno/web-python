from django.db import models

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=10)
    quantidade = models.IntegerField

    def __str__(self):
        return self.titulo
    
