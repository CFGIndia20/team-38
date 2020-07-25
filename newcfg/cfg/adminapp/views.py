from django.shortcuts import render
from adminapp import forms  
from .models import Skills
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

def taskadd(request):

	if request.method =='POST':
		form = forms.TaskForm(request.POST)
		if form.is_valid():

		
			record=form.save(commit=False)

			r=Skills.objects.filter(skill_name=form.cleaned_data['task_skill']).values_list('skill_hour', flat=True)
			r=list(r)
			
			record.task_total_hour= int(r[0]) * int(record.task_quantity)
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

	skill=task_skill


def progress(request):

	return render(request,'admin/taskprogress.html')






































