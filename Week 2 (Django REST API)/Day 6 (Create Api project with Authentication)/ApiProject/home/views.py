from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
# Create your views here.

class Hello(APIView):
    def get(self, request):
        return Response({"message": "Hello, World"})

from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import TokenAuthentication

class TaskAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many = True)
        print(serializer)
        return Response({'status': 200, 'payload': serializer.data})
        pass
    def post(self, request):
        data = request.data
        serializer = TaskSerializer(data = request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': serializer.errors, 'message': 'Something went wronge'})
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message': 'you sent this data'})
        pass 
    def put(self, request):
     try:
        tasks_obj = Task.objects.get(id = request.data["id"])
        serializer = TaskSerializer(tasks_obj, data = request.data)
        if not serializer.is_valid():
             return Response({'status': 403, 'errros': serializer.errors, 'message': "something  went wrong"})
        serializer.save()
        return Response ({"status": 200, 'payload': serializer.data, "message": "Updated Successfully"})
     except Exception as e:
        return Response({"status": 403, 'message': 'invalid id'})
        pass
    def delete(self, request):
     try: 
        id = request.GET.get('id')
        Task_obj = Task.objects.get(id = id)
        Task_obj.delete()
        return Response ({'status': 200, 'message': 'Task Deleted Successfully'})
     except Exception as e:
        return Response ({'status': 403, 'message': 'Invalid Id in delete operation'})
        pass    