from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from gerencia.models import  Aluno
from gerencia.serializers import AlunoSerializer

@csrf_exempt
def AlunoApi(request,id=0):
    if request.method=='GET':
        aluno = Aluno.objects.all()
        aluno_serializer = AlunoSerializer(aluno,many=True)
        return JsonResponse(aluno_serializer.data,safe=False)
    
    elif request.method=='POST':
        aluno_data=JSONParser().parse(request)
        aluno_serializer=AlunoSerializer(data=aluno_data)
        if aluno_serializer.is_valid():
            aluno_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Falied to Add",safe=False)
    
    elif request.method=='PUT':
        aluno_data=JSONParser().parse(request)
        aluno=Aluno.objects.get(id_aluno=aluno_data['id_aluno'])
        aluno_serializer=AlunoSerializer(aluno,data=aluno_data)
        if aluno_serializer.is_valid():
            aluno_serializer.save()
            return JsonResponse("Update successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        aluno=Aluno.objects.get(id_aluno=id)
        aluno.delete()
        return JsonResponse("Deleted Successfully",safe=False)
