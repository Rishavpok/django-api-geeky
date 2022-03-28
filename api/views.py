from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api import serializers
# Create your views here.

@api_view(['GET'])
def student_list(request):
    student=Student.objects.all()
    student_ser=StudentSerializers(student,many=True)
    return Response({
        "status":True,
        "data":student_ser.data
    },200)
 

