from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from gerencia.models import Professor
from gerencia.serializers import ProfessorSerializer

@csrf_exempt
def ProfessorApi(request,id=0):
    if request.method=='GET':
        professor = Professor.objects.all()
        professor_serializer = ProfessorSerializer(professor,many=True)
        return JsonResponse(professor_serializer.data,safe=False)
    
    elif request.method=='POST':
        professor_data=JSONParser().parse(request)
        professor_serializer=ProfessorSerializer(data=professor_data)
        if professor_serializer.is_valid():
            professor_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Falied to Add",safe=False)
    
    elif request.method=='PUT':
        professor_data=JSONParser().parse(request)
        professor=Professor.objects.get(id_professor=professor_data['id_professor'])
        professor_serializer=ProfessorSerializer(professor,data=professor_data)
        if professor_serializer.is_valid():
            professor_serializer.save()
            return JsonResponse("Update successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        professor=Professor.objects.get(id_professor=id)
        try: 
            professor.delete()
            return JsonResponse("Deleted Successfully",safe=False)
        except:
            return JsonResponse("Deleted Failed")