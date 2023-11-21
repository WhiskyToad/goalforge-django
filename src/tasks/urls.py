from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [path("api/tasks/", views.TasksViews.as_view(), name="tasks")]
