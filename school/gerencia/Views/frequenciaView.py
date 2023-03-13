from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from gerencia.models import Frequencia
from gerencia.serializers import FrequenciaSerializer

@csrf_exempt
def FrequenciaApi(request,id=0):
    if request.method=='GET':
        frequencia = Frequencia.objects.all()
        frequencia_serializer = FrequenciaSerializer(frequencia,many=True)
        return JsonResponse(frequencia_serializer.data,safe=False)
    
    elif request.method=='POST':
        frequencia_data=JSONParser().parse(request)
        frequencia_serializer=FrequenciaSerializer(data=frequencia_data)
        if frequencia_serializer.is_valid():
            frequencia_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Falied to Add",safe=False)
    
    elif request.method=='PUT':
        frequencia_data=JSONParser().parse(request)
        frequencia=Frequencia.objects.get(id_frequencia=frequencia_data['id_frequencia'])
        frequencia_serializer=FrequenciaSerializer(frequencia,data=frequencia_data)
        if frequencia_serializer.is_valid():
            frequencia_serializer.save()
            return JsonResponse("Update successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        frequencia=Frequencia.objects.get(id_frequencia=id)
        frequencia.delete()
        return JsonResponse("Deleted Successfully",safe=False)