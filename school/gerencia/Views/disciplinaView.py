from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from gerencia.models import Disciplina
from gerencia.serializers import DisciplinaSerializer


@csrf_exempt
def DisciplinaApi(request,id=0):
    if request.method=='GET':
        disciplina = Disciplina.objects.all()
        disciplina_serializer = DisciplinaSerializer(disciplina,many=True)
        return JsonResponse(disciplina_serializer.data,safe=False)
    
    elif request.method=='POST':
        disciplina_data=JSONParser().parse(request)
        disciplina_serializer=DisciplinaSerializer(data=disciplina_data)
        if disciplina_serializer.is_valid():
            disciplina_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Falied to Add",safe=False)
    
    elif request.method=='PUT':
        disciplina_data=JSONParser().parse(request)
        disciplina=Disciplina.objects.get(id_disciplina=disciplina_data['id_disciplina'])
        disciplina_serializer=DisciplinaSerializer(disciplina,data=disciplina_data)
        if disciplina_serializer.is_valid():
            disciplina_serializer.save()
            return JsonResponse("Update successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        disciplina=Disciplina.objects.get(id_disciplina=id)
        disciplina.delete()
        return JsonResponse("Deleted Successfully",safe=False)