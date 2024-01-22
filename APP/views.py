from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class StudentDetail(APIView):
    def get(self,request):
        obj = Student.objects.all()
        serializer = Studentserializers(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = Studentserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

class StudentInfo(APIView):
    def get(self, request, id):
        try:
            obj = Student.objects.get(id=id)

        except Student.DoesNotExist:
            msg = {"msg" : "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = Studentserializers(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        try:
            obj = Student.objects.get(id=id)

        except Student.DoesNotExist:
            msg = {"msg" : "not found error"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = Studentserializers(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        try:
            obj = Student.objects.get(id=id)

        except Student.DoesNotExist:
            msg = {"msg" : "not found error"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = Studentserializers(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            obj = Student.objects.get(id=id)

        except StudentDetail.DoesNotExist:
            msg = {"msg" : "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)  

        obj.delete()
        return Response({"msg" : "deleted"}, status=status.HTTP_204_NO_CONTENT)  