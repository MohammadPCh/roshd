from django.db.models import Avg
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from school.models import *
from school.serializers import MarkSerializer, StudentSerializer


class StudentMarkAPI(APIView):

    def get(self, request, nid):
        marks = Mark.objects.filter(student__nid=nid)
        serializer = MarkSerializer(marks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClassRoomStudentListAPI(APIView):

    def get(self, request, name, year):
        students = Student.objects.filter(classroom__class_name=name, students__semester__year=year)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CourseAverageAPI(APIView):

    def get(self, request, name, year):
        offers = OfferedCourse.objects.filter(course__name=name)
        result = []
        for offer in offers:
            detail = dict()
            classroom = offer.classroom
            semester = offer.semester
            avg = Mark.objects.filter(course__offeredcourse=offer)\
                .filter(semester=semester)\
                .filter(classroom=classroom)\
                .aggregate(Avg('mark'))
            detail['Classroom'] = str(classroom)
            detail['Semester'] = str(semester)
            detail['Average'] = avg['mark__avg']
            result.append(detail)

        return Response(result, status=status.HTTP_200_OK)
