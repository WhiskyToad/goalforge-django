from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TasksViewSet

app_name = "tasks"

router = DefaultRouter()
router.register(r"api/tasks", TasksViewSet, basename="tasks")
urlpatterns = router.urls
