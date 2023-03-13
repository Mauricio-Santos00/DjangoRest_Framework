from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from gerencia.models import Atividade
from gerencia.serializers import AtividadeSerializer


@csrf_exempt
def AtividadeApi(request,id=0):
    if request.method=='GET':
        atividade = Atividade.objects.all()
        atividade_serializer = AtividadeSerializer(atividade,many=True)
        return JsonResponse(atividade_serializer.data,safe=False)
    
    elif request.method=='POST':
        atividade_data=JSONParser().parse(request)
        atividade_serializer=AtividadeSerializer(data=atividade_data)
        if atividade_serializer.is_valid():
            atividade_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Falied to Add",safe=False)
    
    elif request.method=='PUT':
        atividade_data=JSONParser().parse(request)
        atividade=Atividade.objects.get(id_atividade=atividade_data['id_atividade'])
        atividade_serializer=AtividadeSerializer(atividade,data=atividade_data)
        if atividade_serializer.is_valid():
            atividade_serializer.save()
            return JsonResponse("Update successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        atividade=Atividade.objects.get(id_atividade=id)
        atividade.delete()
        return JsonResponse("Deleted Successfully",safe=False)