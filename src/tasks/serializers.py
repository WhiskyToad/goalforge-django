from rest_framework import serializers
from .models import Task


# Serializers define the API representation.
class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
