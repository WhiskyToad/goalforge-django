from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TasksViewSet

app_name = "tasks"

router = DefaultRouter()
router.register(r"api/tasks", TasksViewSet, basename="tasks")

urlpatterns = [
    path(
        "api/tasks/tasks_for_day/",
        TasksViewSet.as_view({"get": "tasks_for_day"}),
        name="tasks-for-day",
    ),
    path(
        "api/tasks/create_task/",
        TasksViewSet.as_view({"post": "create_task"}),
        name="create-task",
    ),
    path(
        "api/tasks/<int:pk>/update_task/",
        TasksViewSet.as_view({"put": "update_task"}),
        name="update-task",
    ),
    path(
        "api/tasks/<int:pk>/delete_task/",
        TasksViewSet.as_view({"delete": "delete_task"}),
        name="delete-task",
    ),
    path(
        "api/tasks/<int:pk>/complete_task/",
        TasksViewSet.as_view({"post": "complete_task"}),
        name="complete-task",
    ),
]
urlpatterns += router.urls
