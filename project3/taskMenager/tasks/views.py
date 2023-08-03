from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Task
from .forms import TaskForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

# widok zadań dla wybranego użytkownika
def tasks(request):
    userTasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks.html', {'Tasks': userTasks})

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
    
