from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .models import Task
from .forms import TaskForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')


# widok zadań dla wybranego użytkownika
@login_required
def tasks(request):
    currentTasks = Task.objects.filter(user=request.user,
                                       completeDate__isnull=True)
    complitedTasks = Task.objects.filter(user=request.user,
                                         completeDate__isnull=False)
    return render(request, 'tasks.html', {'current': currentTasks, 'complited': complitedTasks})


@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'createTask.html', {'Form': TaskForm})
    else:  # post
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # dodanie zalogowanego użytkowanika do danego taska
            task.save()
            return redirect('tasks')
        else:
            error = "Something went wrong"
            return render(request, 'createTask.html', {'Form': TaskForm, 'Error': error})


@login_required
def deleteTask(request, taskID):
    task = get_object_or_404(Task, id=taskID, user=request.user)
    task.delete()
    return redirect('tasks')


@login_required
def detailTask(request, taskID):
    task = get_object_or_404(Task, id=taskID, user=request.user)
    if request.method == 'GET':
        form = TaskForm(instance=task)  #formulaż wypełni się danymi z task
        return render(request, 'detailTask.html', {'form': form, 'task': task})
    else:  # POST
        form = TaskForm(request.POST, instance=task)  # formula
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else:
            error = 'Something went wrong.'
            return render(request, 'detailTask.html', {'form': form, 'task': task, 'error': error})


@login_required
def completeTask(request,taskID):
    task = get_object_or_404(Task, id=taskID, user=request.user)
    task.completeDate = timezone.now()
    task.save()
    return redirect('tasks')
