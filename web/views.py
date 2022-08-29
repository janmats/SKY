from django.http import HttpResponse
from django.shortcuts import render

sotrydnik_data=[
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
    return render(request, 'index.html', {'sotrydniks':sotrydnik_data})
def groups(request):
    return render(request, 'groups.html')
def help(request):
    return render(request, 'help.html')


