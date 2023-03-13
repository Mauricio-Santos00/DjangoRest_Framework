from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from gerencia.models import FrequenciaAluno
from gerencia.serializers import FrequenciaAlunoSerializer

@csrf_exempt
def FrequenciaAlunoApi(request,id=0):
    if request.method=='GET':
        frequencia_aluno = FrequenciaAluno.objects.all()
        frequencia_aluno_serializer = FrequenciaAlunoSerializer(frequencia_aluno,many=True)
        return JsonResponse(frequencia_aluno_serializer.data,safe=False)
    
    elif request.method=='POST':
        frequencia_aluno_data=JSONParser().parse(request)
        frequencia_aluno_serializer=FrequenciaAlunoSerializer(data=frequencia_aluno_data)
        if frequencia_aluno_serializer.is_valid():
            frequencia_aluno_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Falied to Add",safe=False)
    
    elif request.method=='PUT':
        frequencia_aluno_data=JSONParser().parse(request)
        frequencia_aluno=FrequenciaAluno.objects.get(id=frequencia_aluno_data['id'])
        frequencia_aluno_serializer=FrequenciaAlunoSerializer(frequencia_aluno,data=frequencia_aluno_data)
        if frequencia_aluno_serializer.is_valid():
            frequencia_aluno_serializer.save()
            return JsonResponse("Update successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        frequencia=FrequenciaAluno.objects.get(id=id)
        frequencia.delete()
        return JsonResponse("Deleted Successfully",safe=False)