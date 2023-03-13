from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from gerencia.models import DisciplinaAluno
from gerencia.serializers import DisciplinaAlunoSerializer

@csrf_exempt
def DisciplinaAlunoApi(request,id=0):
    if request.method=='GET':
        disciplina_aluno = DisciplinaAluno.objects.all()
        disciplina_aluno_serializer = DisciplinaAlunoSerializer(disciplina_aluno,many=True)
        return JsonResponse(disciplina_aluno_serializer.data,safe=False)
    
    elif request.method=='POST':
        disciplina_aluno_data=JSONParser().parse(request)
        disciplina_aluno_serializer=DisciplinaAlunoSerializer(data=disciplina_aluno_data)
        if disciplina_aluno_serializer.is_valid():
            disciplina_aluno_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Falied to Add",safe=False)
    
    elif request.method=='PUT':
        disciplina_aluno_data=JSONParser().parse(request)
        disciplina_aluno=DisciplinaAluno.objects.get(id_matricula=disciplina_aluno_data['id_matricula'])
        disciplina_aluno_serializer=DisciplinaAlunoSerializer(disciplina_aluno,data=disciplina_aluno_data)
        if disciplina_aluno_serializer.is_valid():
            disciplina_aluno_serializer.save()
            return JsonResponse("Update successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        disciplina_aluno=DisciplinaAluno.objects.get(id_matricula=id)
        disciplina_aluno.delete()
        return JsonResponse("Deleted Successfully",safe=False)