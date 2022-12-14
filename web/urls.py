"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from web import views

urlpatterns = [
    path('', views.index),
    path('groups', views.groups),
    path('help', views.help),
    path('createworker', views.createworker, name='createworker'),
    path('deleteworker/<int:id>', views.deleteworker, name='deleteworker'),
    path("createworkgroup", views.createworkgroup, name='createworkgroup'),
    path('deletewokgroup/<int:id>', views.deleteworkgroup, name='deleteworkgroup'),
    path('editpersonaldata/<int:id>', views.editpersonaldata, name='editpersonaldata')
]
