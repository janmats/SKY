from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from web.models import *

worker_data=[
    {
        'id': '1',
        'name': 'Иванов',
        'position':'Директор',
        'workgroup':'административная группа'
    },
{
        'id': '2',
        'name':'Петров',
        'position':'Менеджер',
        'workgroup':'Менеджерская группа'
    },
{
        'id': '3',
        'name':'Сидоров',
        'position':'уборщик',
        'workgroup':'Клининг группа'
    }
]

def index(request):
    return render(request, 'index.html', {
        'workers':Worker.objects.all()
    })

def groups(request):
    return render(request, 'groups.html')

def help(request):
    return render(request, 'help.html')

def createworker(request):
    if request.method=='GET':
        return render(request, 'createworker.html')
    else:
        name=request.POST['name']
        position = request.POST['position']
        workgroup = request.POST['workgroup']


        Worker(name=name, position=position, workgroup=workgroup).save()

        return redirect('/')


