from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
    return redirect('task_list')

def update_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/update_task.html', {'task': task})

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('task_list')
