from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from web.models import *

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

def deleteworker(request, id):
    if request.method=='POST':
       worker = Worker.objects.get(id=id)
       worker.delete()
       return redirect('/')


