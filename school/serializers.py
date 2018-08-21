from rest_framework import serializers
from school.models import Mark, Student


class MarkSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    course = serializers.StringRelatedField()
    semester = serializers.StringRelatedField()
    classroom = serializers.StringRelatedField()

    class Meta:
        model = Mark
        fields = ["student", "course", "semester", "mark", "classroom", ]


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
