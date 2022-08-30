from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    workgroup = models.CharField(max_length=30)