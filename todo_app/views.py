from django.shortcuts import redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task, Tag
from .forms import TaskForm, TagForm, TaskUpdateForm


class IndexView(ListView):
    model = Task
    template_name = "todo_app/index.html"
    context_object_name = "tasks"
    ordering = ["is_done", "-datetime_created"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_form"] = TaskForm()
        return context

    def post(self, request, *args, **kwargs):
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
        return redirect("todo_list:index")


class AddTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_app/add_task.html"
    success_url = reverse_lazy("todo_list:index")


class UpdateTaskView(UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = "todo_app/update_task.html"

    def get_success_url(self):
        return reverse_lazy("todo_list:index")


class DeleteTaskView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:index")


@method_decorator(require_POST, name="dispatch")
class UndoTaskView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = False
        task.save()
        return redirect("todo_list:index")


class ToggleTaskStatusView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        task.is_done = not task.is_done
        task.save()
        return redirect("todo_list:index")


class TagListView(ListView):
    model = Tag
    template_name = "todo_app/tag_list.html"
    context_object_name = "tags"


class AddTagView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo_app/add_tag.html"
    success_url = reverse_lazy("todo_list:tag-list")


class UpdateTagView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todo_app/update_tag.html"
    success_url = reverse_lazy("todo_list:tag-list")


class DeleteTagView(DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")
