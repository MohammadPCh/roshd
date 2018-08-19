from rest_framework import serializers
from school.models import Mark


class MarksSerializer(serializers.ModelSerilizer):
    class Meta:
        model = Mark
        fields = '__all__'