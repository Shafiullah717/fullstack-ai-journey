from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.authtoken.models import Token
# Create your views here.


class RegisterUser(APIView):
   def post(self, request):
      serializer = UserSerializer(data = request.data)

      if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status' : 403, 'errors': serializer.errors , 'message' : 'Something went wrong'})
      serializer.save()
      user = User.objects.get(username = serializer.data['username'])
      token_obj = Token.objects.create(user = user)

      return Response({'status' : 200, 'payLoad' : serializer.data, 'token': str(token_obj), 'message' :'You sent this data'})
      pass

class Hello(APIView):
   def get(self, request):
      return Response({'status': 200, 'message' : 'Hello world'})
      pass

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 
    def get(self, request):
        Student_objs = Student.objects.all()
        serializer = StudentSerializer(Student_objs, many = True)
        print(serializer.data)
        return Response({'status' : 200, 'payload' : serializer.data})
        
    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data = request.data)
    
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status' : 403, 'errors': serializer.errors , 'message' : 'Something went wrong'})
        serializer.save()

        return Response({'status' : 200, 'payLoad' : serializer.data, 'message' :'You sent this data'})
    def put(self, request):
        try:
         student_obj = Student.objects.get(id = request.data['id'])
         serializers = StudentSerializer(student_obj, data = request.data)

         if not serializers.is_valid():
             return Response({'status' : 403, 'errors': serializers.errors, 'message' :'Something went Wrong'})
         serializers.save()

         return Response({'status' : 200, 'payload' : serializers.data, 'message' : 'You data is   updated successfully'})
        except Exception as e:
         return Response({ 'status' : 403, 'message' : 'invalid id'})
    def patch(self, request):
        try:
         student_obj = Student.objects.get(id = request.data['id'])
         serializers = StudentSerializer(student_obj, data = request.data, partial = True)

         if not serializers.is_valid():
             return Response({'status' : 403, 'errors': serializers.errors, 'message' :'Something went Wrong'})
         serializers.save()

         return Response({'status' : 200, 'payload' : serializers.data, 'message' : 'You data is   updated successfully'})
        except Exception as e:
         return Response({ 'status' : 403, 'message' : 'invalid id'})
    def delete(self, request):
       try:
         id = request.GET.get('id')
         student_obj = Student.objects.get(id = id)
         student_obj.delete()
         return Response({'status' : 200, 'message' : 'student deleted successfully'})
    
       except Exception as e:
         return Response({'status' : 403, 'message' : 'invalid id'})   
        









# @api_view(['GET'])
# def home(request):
#     studen_objs = Student.objects.all()
#     serializer = StudentSerializer(studen_objs, many = True)
#     return Response({'status': 200, "payload" : serializer.data})





























# @api_view(['POST'])
# def add_student(request):
#     serializer = StudentSerializer(data = request.data)

#     if not serializer.is_valid():
#         print(serializer.errors)
#         return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something went wrong'})
#     serializer.save()

#     return Response({'status': 200, 'payload': serializer.data, 'message': 'data save successfully'})