from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Task
from .serializers import TasksSerializer


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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["put"])
    def update_task(self, request, pk=None):
        task = self.get_object()
        serializer = TasksSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["delete"])
    def delete_task(self, request, pk=None):
        task = self.get_object()
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=["post"])
    def complete_task(self, request, pk=None):
        task = self.get_object()
        task.completed = True
        task.save()
        return Response(
            {"message": "Task marked as completed"}, status=status.HTTP_200_OK
        )
