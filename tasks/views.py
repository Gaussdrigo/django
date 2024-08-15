from django.shortcuts import render, redirect
from .models import Task


def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, "list_tasks.html", {"tasks": tasks})


def add_task(request):
    if request.method == "POST":
        task_name = request.POST.get("task_name")
        task_description = request.POST.get("task_description")

        Task.objects.create(name=task_name, description=task_description)
        return redirect("list_tasks")
    return redirect("list_tasks")


from django.shortcuts import get_object_or_404


def delete_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect("list_tasks")
    else:
        # Opcional: Puedes manejar una redirección o mensaje de error si el método no es POST
        return redirect("list_tasks")
