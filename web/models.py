from django.db import models

class Workgroup(models.Model):
    name = models.CharField(max_length=30)

class Worker(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    workgroup = models.ForeignKey(Workgroup, on_delete=models.CASCADE)

class Personaldata(models.Model):
    worker = models.OneToOneField(Worker, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True)
    address = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=True)
