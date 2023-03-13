from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from gerencia.models import PlanoAula
from gerencia.serializers import PlanoAulaSerializer


@csrf_exempt
def PlanoAulaApi(request,id=0):
    if request.method=='GET':
        plano_aula = PlanoAula.objects.all()
        plano_aula_serializer = PlanoAulaSerializer(plano_aula,many=True)
        return JsonResponse(plano_aula_serializer.data,safe=False)
    
    elif request.method=='POST':
        plano_aula_data=JSONParser().parse(request)
        plano_aula_serializer=PlanoAulaSerializer(data=plano_aula_data)
        if plano_aula_serializer.is_valid():
            plano_aula_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Falied to Add",safe=False)
    
    elif request.method=='PUT':
        plano_aula_data=JSONParser().parse(request)
        plano_aula=PlanoAula.objects.get(id_plano_aula=plano_aula_data['id_plano_aula'])
        plano_aula_serializer=PlanoAulaSerializer(plano_aula,data=plano_aula_data)
        if plano_aula_serializer.is_valid():
            plano_aula_serializer.save()
            return JsonResponse("Update successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        plano_aula=PlanoAula.objects.get(id_plano_aula=id)
        plano_aula.delete()
        return JsonResponse("Deleted Successfully",safe=False)