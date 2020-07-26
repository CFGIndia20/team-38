from django.db import models
from datetime import date
from django.utils import timezone
# Create your models here.
from django.core.validators import RegexValidator,MinValueValidator

class Session(models.Model):


        session_date=models.DateTimeField(blank=True,default=timezone.now)
        session_name=models.CharField(max_length=500)
        session_location=models.CharField(max_length=200)
        session_description=models.CharField(max_length=500)
        
        session_file = models.FileField(upload_to='session_files/',blank=True,null=True)
        session_duration=models.IntegerField(validators=[MinValueValidator(0, message="Amount should be more than 0")])
      	
class Task(models.Model):


        task_name=models.CharField(max_length=500)
        task_quantity=models.CharField(max_length=200)
        

        task_choices = [
        ('Skill1', 'Skill1'),
        ('Skill2', 'Skill2'),
       	('Skill3', 'Skill3'),
        
        ]
        task_skill=models.CharField(
        max_length=100,
        choices=task_choices,
        default='Skill1',
        )
        
        task_total_hour=models.IntegerField(default=0,validators=[MinValueValidator(0, message="Amount should be more than 0")])
        hpu=models.IntegerField(validators=[MinValueValidator(0, message="Amount should be more than 0")])

        def __str__(self):
            return self.task_name



class Skills(models.Model):

    skill_name=models.CharField(max_length=500)
    skill_hour=models.IntegerField()



class CurrentTask(models.Model):

    task_name = models.CharField(max_length=100)
    username=models.CharField(max_length=500)
    













