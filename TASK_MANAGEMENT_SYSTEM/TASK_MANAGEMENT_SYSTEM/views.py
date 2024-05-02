from django.shortcuts import render,redirect
from task.models import TaskModel

def show_tasks(request):
    datas = TaskModel.objects.all()
    return render(request,'home.html', {'datas' : datas})