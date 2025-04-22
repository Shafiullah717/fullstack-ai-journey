from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import StudentSerializer
# Create your views here.

@api_view(['GET'])
def home(request):
    studen_objs = Student.objects.all()
    serializer = StudentSerializer(studen_objs, many = True)
    return Response({'status': 200, "payload" : serializer.data})

@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializer(data = request.data)

    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something went wrong'})
    serializer.save()

    return Response({'status': 200, 'payload': serializer.data, 'message': 'data save successfully'})