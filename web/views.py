from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from web.models import *
from django.utils.dateparse import parse_date


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
        #Worker(name=name, position=position, workgroup=workgroup).save()
        worker = Worker(name=name, position=position, workgroup=workgroup)
        worker.save()
        date = request.POST['birthdate']
        birthdate = parse_date(date)
        address = request.POST['address']
        email = request.POST['email']
        Personaldata(worker=worker, birthdate=birthdate, address=address, email=email).save()
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

def deleteworkgroup(request, id):
    if request.method=='POST':
       workgroup = Workgroup.objects.get(id=id)
       workgroup.delete()
       return redirect('/groups')


def editpersonaldata(request, id):
    if request.method=='GET':
        if Personaldata.objects.filter(worker_id=id).exists():
           return render(request, 'editpersonaldata.html', {
           'worker':Worker.objects.get(id=id),
           'personaldata':Personaldata.objects.get(worker_id=id)
       })
        else:
            worker = Worker.objects.get(id=id)
            personaldata = Personaldata(worker=worker, birthdate=None, address=None, email=None).save()
            return render(request, 'editpersonaldata.html', {
                'worker': Worker.objects.get(id=id),
                'personaldata': personaldata
            })
    else:
        if request.method=='POST':

            worker = Worker.objects.get(id=id)
            personaldata = Personaldata.objects.get(worker=worker)
            date = request.POST['birthdate']
            personaldata.birthdate = parse_date(date)
            personaldata.address = request.POST['address']
            personaldata.email = request.POST['email']
            personaldata.save()
            return redirect('/')


