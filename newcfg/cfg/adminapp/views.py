from django.shortcuts import render,redirect
from adminapp import forms  
from .models import Skills,Task,CurrentTask
from .forms import TaskForm
from django.http import HttpResponseRedirect 
from django.urls import reverse
from women.models import Women
#from rest_framework.decorators import api_view 
# Create your views here.

def sessionadd(request):

	if request.method =='POST':
		form = forms.SessionForm(request.POST,request.FILES)
		if form.is_valid():

			record=form.save()

			record.save()

			form=forms.SessionForm()

		else:
			print(form.errors)

	else:
		form=forms.SessionForm()

	return render(request,'admin/session.html',{'form': form})

# @api_view(['POST'])
def taskadd(request):
	#import pdb;pdb.set_trace()
	if request.method =='POST':
		form = forms.TaskForm(request.POST)
		if form.is_valid():

			record=form.save(commit=False)
			print(record)
			record.task_total_hour= int(record.hpu) * int(record.task_quantity)
			record.save()

			form=forms.TaskForm()

		else:
			print(form.errors)

	else:
		form=forms.TaskForm()


	r=Task.objects.all()


	return render(request,'admin/task.html',{'form': form,'r':r})

	


def assigntask(request,i):

	# r= Task.objects.get(id=id)

	# hours=r.task_total_hour

	# skill=r.task_skill
	r = 3
	tname="task1"
	hours=10
	skill="Skill1"
	women=Women.objects.filter(available=True)
	# no_of_women=len(women)
	# total=Women.objects.filter(available=True).aggregate(Sum('hours_available'))

	# if total>hours:

	# 	eachhour=hours//no_of_women
	allocated=CurrentTask.objects.filter(task_name=tname).distinct()
	print(allocated)


	return render(request,'admin/allocation.html',{'women':women,'tname':tname,'all':allocated})


def taskallocation(request,uname,tname):

	Women.objects.filter(fname=uname).update(available=False)
	p = CurrentTask(task_name=tname,username=uname)
	p.save()

	
	return redirect("/adm/assigntask/1/")



def progress(request):

	return redirect("/adm/progress")



def attendance(request):

	return render(request,'admin/attendanceAdmin.html')




































