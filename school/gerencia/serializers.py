from rest_framework import serializers
from gerencia.models import Professor, Aluno, Disciplina, Atividade, AtividadeAluno, PlanoAula, Frequencia, FrequenciaAluno, DisciplinaAluno

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Professor
        fields=('id_professor','nome','cpf','rg','codigo','email','telefone')
        
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Aluno
        fields=('id_aluno','nome','cpf','rg','matricula','email','telefone')
        
class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Disciplina
        fields=('id_disciplina','id_professor','nome','codigo','carga_horaria','ementa')

class AtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Atividade
        fields=('id_atividade','atividade','tipo','data_postagem','data_entrega','id_disciplina','id_plano_aula')
        
class AtividadeAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model=AtividadeAluno
        fields=('id','id_atividade','id_aluno','nota')
        
class DisciplinaAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model=DisciplinaAluno
        fields=('id_matricula','id_aluno','id_disciplina','nota')
        
class PlanoAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlanoAula
        fields=('id_plano_aula','id_disciplina','tema_aula','conteudo','metodo','dia')
        
class FrequenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Frequencia
        fields=('id_frequencia','id_materia','dia')
        
class FrequenciaAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model=FrequenciaAluno
        fields=('id','id_aluno','id_frequencia','presenca')