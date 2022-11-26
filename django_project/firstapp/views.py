from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from firstapp.serializers import studentserializer
# Create your views here.
def welcome_view(request):
    return HttpResponse("<h2 style='color:yellow'>welcome to Django</h2>")

# class school:
@api_view(['post'])
def add_student(request):
    print(request.data)
    serializer=studentserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=HTTP_200_OK)
    return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)