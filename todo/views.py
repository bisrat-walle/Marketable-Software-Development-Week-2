from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    tasks_list = Task.objects.order_by('date_created')
    if request.method == "POST":
        data = request.POST
        task_form = TaskForm(data)
        if task_form.is_valid():
            task_form.save()
            messages.info(request, 'Task Item created!')
            redirect('tasks')
    task_form = TaskForm()
    context = {
        "form": task_form,
        "tasks": tasks_list,
    }
    return render(request, 'todo/index.html', context)
    

def remove_task(request, task_id):
    task = Task.objects.filter(id=task_id)
    if task.exists():
        task.delete()
    messages.info(request, 'Task Item removed!')
    return redirect('tasks')


