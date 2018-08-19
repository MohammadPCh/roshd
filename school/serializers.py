from rest_framework import serializers
from school.models import Mark


class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'
