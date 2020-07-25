from django.shortcuts import render
from adminapp import forms  
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
		form = forms.TaskForm(request.POST,request.FILES)
		if form.is_valid():

			record=form.save()

			record.save()

			form=forms.TaskForm()

		else:
			print(form.errors)

	else:
		form=forms.TaskForm()

	return render(request,'admin/task.html',{'form': form})

	











