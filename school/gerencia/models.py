from django.db import models
from django import forms 

class Professor(models.Model):
    id_professor = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255,null=False)
    cpf = models.CharField(max_length=11,null=False)
    rg = models.CharField(max_length=8,null=False)
    codigo = models.CharField(max_length=8,null=False)
    email = models.CharField(max_length=255,null=False)
    telefone = models.CharField(max_length=11,null=False)

class Aluno(models.Model):
    id_aluno = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255,null=False)
    cpf = models.CharField(max_length=11,null=False)
    rg = models.CharField(max_length=8,null=False)
    matricula = models.CharField(max_length=8,null=False)
    email = models.CharField(max_length=255,null=False)
    telefone = models.CharField(max_length=11,null=False)

class Disciplina(models.Model):
    id_disciplina = models.IntegerField(primary_key=True)
    id_professor = models.ForeignKey(Professor,on_delete=models.CASCADE)
    nome = models.CharField(max_length=255,null=False)
    codigo = models.CharField(max_length=7,null=False)
    carga_horaria = models.IntegerField(null=False)
    ementa = models.BinaryField(blank=True)

class PlanoAula(models.Model):
    id_plano_aula = models.IntegerField(primary_key=True)
    id_disciplina = models.ForeignKey("Disciplina",on_delete=models.CASCADE)
    tema_aula = models.CharField(max_length=255)
    conteudo = models.BinaryField(null=False)
    metodo = models.CharField(max_length=50)
    dia = models.DateTimeField(null=False)

class Frequencia(models.Model):
    id_frequencia = models.IntegerField(primary_key=True)
    id_disciplina = models.ForeignKey("Disciplina", on_delete=models.CASCADE)
    dia = models.DateField(null=False)

class Atividade(models.Model):
    id_atividade = models.IntegerField(primary_key=True)
    atividade = models.BinaryField(blank=False)
    tipo = models.CharField(max_length=50,null=False)
    data_postagem = models.DateField(null=False)
    data_entrega = models.DateField(blank=True)
    id_disciplina = models.ForeignKey("Disciplina",on_delete=models.CASCADE)
    id_plano_aula = models.ForeignKey("PlanoAula",on_delete=models.CASCADE)
    
class FrequenciaAluno(models.Model):
    id = models.IntegerField(primary_key=True)
    id_aluno = models.ForeignKey("Aluno", on_delete=models.CASCADE)
    id_frequencia = models.ForeignKey("Frequencia", on_delete=models.CASCADE)
    presenca = models.CharField(max_length=1)
    
class DisciplinaAluno(models.Model):
    id_matricula = models.IntegerField(primary_key=True)
    id_aluno = models.ForeignKey("Aluno",on_delete=models.CASCADE,related_name="Alunos")
    id_disciplina = models.ForeignKey("Disciplina",on_delete=models.CASCADE,related_name="Disciplinas")
    nota = models.FloatField()

class AtividadeAluno(models.Model):
    id = models.IntegerField(primary_key=True)
    id_atividade = models.ForeignKey("Atividade", on_delete=models.CASCADE)
    id_aluno = models.ForeignKey("Aluno",on_delete=models.CASCADE)
    nota = models.FloatField(null=False)
    
class ModeloForm(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=11)
    descricao = models.CharField(max_length=500)