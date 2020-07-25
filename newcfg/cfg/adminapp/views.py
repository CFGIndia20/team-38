from django.shortcuts import render,redirect
from adminapp import forms  
from .models import Skills,Task
from .forms import TaskForm
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

	return render(request,'admin/task.html',{'form': form})

	


def assigntask(request,id):

	r= Task.objects.get(id=id)

	hours=r.task_total_hour

	skill=r.task_skill

	people = .objects.raw('SELECT *, age(birth_date) AS age FROM myapp_person')













	


def progress(request):

	return redirect("/adm/progress")



def attendance(request):

	return render(request,'admin/attendanceAdmin.html')




































