from rest_framework import serializers
from school.models import Mark


class MarkSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    course = serializers.StringRelatedField()
    semester = serializers.StringRelatedField()

    class Meta:
        model = Mark
        fields = '__all__'
