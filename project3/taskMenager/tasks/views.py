from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .models import Task
from .forms import TaskForm
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'home.html')

# widok zadań dla wybranego użytkownika
def tasks(request):
    currentTasks = Task.objects.filter(user=request.user,
                                       completeDate__isnull=True)
    complitedTasks = Task.objects.filter(user=request.user,
                                       completeDate__isnull=False)
    return render(request, 'tasks.html', {'current': currentTasks, 'complited':complitedTasks})

def create_task(request):
    if request.method == 'GET':
        return render(request, 'createTask.html', {'Form': TaskForm})
    else: #post
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user #dodanie zalogowanego użytkowanika do danego taska
            task.save()
            return redirect('tasks')
        else:
            error = "Something went wrong"
            return render(request, 'createTask.html', {'Form': TaskForm, 'Error': error})
    
def deleteTask(request, taskID):
    task = get_object_or_404(Task, id = taskID)
    task.delete()
    return redirect('tasks')


def detailTask(request, taskID):
    task = get_object_or_404(Task, id = taskID)
    if request.method == 'GET':
        form = TaskForm(instance=task) #formulaż wypełni się danymi z task
        return render(request, 'detailTask.html', {'form': form, 'task': task})
    else: #POST
        form = TaskForm(request.POST, instance=task) #formula
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else:
            error = 'Something went wrong.'
            return render(request, 'detailTask.html', {'form': form, 'task': task, 'error': error})


def completeTask(request, taskID):
    task = get_object_or_404(Task, id = taskID)
    task.completeDate = timezone.now()
    task.save()
    return redirect('tasks')
