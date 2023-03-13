from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from gerencia.models import Professor, Disciplina,DisciplinaAluno, Aluno
from gerencia.serializers import ProfessorSerializer, DisciplinaSerializer, AlunoSerializer

@csrf_exempt

def ProfessorDisciplinaApi(request, id = 0):
    if request.method=='GET':
        disciplina = Disciplina.objects.filter(id_professor__id_professor=id)
        disciplina_serializer = DisciplinaSerializer(disciplina, many=True)
        return JsonResponse(disciplina_serializer.data,safe=False)
    
def AlunoDisciplinaApi(request, id = 0):
    if request.method == 'GET':
        aluno = Aluno.objects.filter(Alunos__id_disciplina=id)
        aluno_serializer=AlunoSerializer(aluno,many=True)
        return JsonResponse(aluno_serializer.data,safe=False)
    
