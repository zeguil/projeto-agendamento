from django.db import models
import random
import string

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)

class Reserva(models.Model):
    laboratorio = models.CharField(max_length=255)
    data = models.DateTimeField()
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    codigo_boleto = models.CharField(max_length=20, blank=True, null=True)
