from django.shortcuts import render,redirect
from .forms import TaskForm
from . import models
# Create your views here.

def add_tasks(request):
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('show_task')
    else:
        form = TaskForm()
    return render(request, 'task/add_task.html' , {'form' : form})

def edit_task(request,id):
    task = models.TaskModel.objects.get(pk=id)
    task.is_Completed = True
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('show_task')
    return render(request, 'task/add_task.html' , {'form' : form})

def delete_task(request, id):
    task = models.TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('show_task')

