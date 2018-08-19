from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from school.models import Mark, Student
from school.serializers import MarkSerializer, StudentSerializer


class StudentMarkAPI(APIView):

    def get(self, request, nid):
        marks = Mark.objects.filter(student__nid=nid)
        serializer = MarkSerializer(marks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClassRoomStudentListAPI(APIView):

    def get (self, request, name, year):
        students = Student.objects.filter(classroom__class_name=name, students__semester__year=year)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

