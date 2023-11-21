from rest_framework import viewsets
from .models import Task
from .serializers import TasksSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer

    @action(detail=False, methods=["get"])
    def tasks_for_day(self, request):
        date_param = self.request.query_params.get("date")
        tasks = Task.objects.filter(due_date=date_param)
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["post"])
    def create_task(self, request):
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
