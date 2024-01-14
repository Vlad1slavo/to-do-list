from django.urls import path

from .views import (
    IndexView,
    UpdateTaskView,
    DeleteTaskView,
    TagListView,
    AddTagView,
    UpdateTagView,
    DeleteTagView,
    AddTaskView,
    ToggleTaskStatusView,
    UndoTaskView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("add_task/", AddTaskView.as_view(), name="add-task"),
    path(
        "update_task/<int:pk>/",
        UpdateTaskView.as_view(),
        name="update-task"
    ),
    path(
        "delete_task/<int:pk>/",
        DeleteTaskView.as_view(),
        name="delete-task"
    ),
    path("undo-task/<int:pk>/",
         UndoTaskView.as_view(),
         name="undo-task"
         ),
    path(
        "toggle_task_status/<int:task_id>/",
        ToggleTaskStatusView.as_view(),
        name="toggle-task-status",
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("add_tag/", AddTagView.as_view(), name="add-tag"),
    path("update_tag/<int:pk>/", UpdateTagView.as_view(), name="update-tag"),
    path("delete_tag/<int:pk>/", DeleteTagView.as_view(), name="delete-tag"),
]


app_name = "todo_list"
