from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from web.models import *

def index(request):
    return render(request, 'index.html', {
        'workers':Worker.objects.all()
    })

def groups(request):
    return render(request, 'groups.html', {
        'workgroups':Workgroup.objects.all()
    })

def help(request):
    return render(request, 'help.html')

def createworker(request):
    if request.method=='GET':
        return render(request, 'createworker.html', {
        'workgroups':Workgroup.objects.all()
    })
    else:
        name=request.POST['name']
        position = request.POST['position']
        workgroupname = request.POST['workgroup']
        workgroup = Workgroup.objects.get(name=workgroupname)

        Worker(name=name, position=position, workgroup=workgroup).save()

        return redirect('/')

def deleteworker(request, id):
    if request.method=='POST':
       worker = Worker.objects.get(id=id)
       worker.delete()
       return redirect('/')

def createworkgroup(request):
        if request.method == 'GET':
            return render(request, 'createworkgroup.html')
        else:
            name = request.POST['name']
            Workgroup(name=name).save()

            return redirect('/groups')


