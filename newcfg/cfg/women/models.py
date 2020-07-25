from django.db import models
from django import forms

# Create your models here.
class Skills(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title


class Women(models.Model):
    fname = models.CharField(max_length=100,default=None)
    lname = models.CharField(max_length=100,default=None)
    location = models.CharField(max_length=200,default=None)
    contact = models.CharField(max_length=10,default=None)
    skillset = models.ForeignKey(Skills,on_delete=models.CASCADE)
    img = models.FileField(default='default.jpg',upload_to='media/profile_pics')

class Task(models.Model):
    task = models.CharField(max_length=50)
    def __str__(self):
        return self.task

class Progression(models.Model):
    name = models.CharField(max_length=100,default=None)
    locationp = models.CharField(max_length=100,default=None)
    curr_work = models.ForeignKey(Task,on_delete=models.CASCADE)
    hrperday = models.CharField(max_length=10,default=None)
    nopro = models.CharField(max_length=10,default=None)
    day = models.CharField(max_length=20,default=None)
    img = models.FileField(default='default.jpg',upload_to='media/progression')





