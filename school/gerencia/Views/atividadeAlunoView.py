from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from gerencia.models import AtividadeAluno
from gerencia.serializers import AtividadeAlunoSerializer

@csrf_exempt
def AtividadeAlunoApi(request,id=0):
    if request.method=='GET':
        atividade_aluno = AtividadeAluno.objects.all()
        atividade_aluno_serializer = AtividadeAlunoSerializer(atividade_aluno,many=True)
        return JsonResponse(atividade_aluno_serializer.data,safe=False)
    
    elif request.method=='POST':
        atividade_aluno_data=JSONParser().parse(request)
        atividade_aluno_serializer=AtividadeAlunoSerializer(data=atividade_aluno_data)
        if atividade_aluno_serializer.is_valid():
            atividade_aluno_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Falied to Add",safe=False)
    
    elif request.method=='PUT':
        atividade_aluno_data=JSONParser().parse(request)
        atividade_aluno=AtividadeAluno.objects.get(id_atividade=atividade_aluno_data['id_atividade'])
        atividade_aluno_serializer=AtividadeAlunoSerializer(atividade_aluno,data=atividade_aluno_data)
        if atividade_aluno_serializer.is_valid():
            atividade_aluno_serializer.save()
            return JsonResponse("Update successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        atividade_aluno=AtividadeAluno.objects.get(id=id)
        atividade_aluno.delete()
        return JsonResponse("Deleted Successfully",safe=False)