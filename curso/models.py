from django.db import models

# Create your models here.


class Modalidade(models.Model):
    nome

class Curso(models.Model):
    nome
    descricao
    vagas
    inscritos
    modalidade


class Aluno(models.Model):
    nome
    email