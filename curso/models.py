from django.db import models

# Create your models here.


class Modalidade(models.Model):
    nome = models.CharField(max_length=255)

class Curso(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    vagas = models.FloatField()
    inscritos = models.FloatField()
    modalidade = models.ForeignKey(Modalidade, on_delete=models)


class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=30)
    data_nascimento = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)