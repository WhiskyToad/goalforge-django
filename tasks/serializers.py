from rest_framework import serializers
from .models import Task


# Serializers define the API representation.
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "completed",
            "completed_at",
            "created_at",
            "attempt_date",
        ]
        lookup_field = "id"
