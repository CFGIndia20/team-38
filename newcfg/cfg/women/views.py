from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.http import *

  

# Create your views here.
def womendetail(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = WomenForm()
        else:
            women = Women.objects.get(pk=id)
            form = WomenForm(instance=women)
        return render(request, "women/womenform.html", {'form': form})
    else:
        if id == 0:
            form = WomenForm(request.POST,request.FILES)
        else:
            women = Women.objects.get(pk=id)
            form = WomenForm(request.POST,instance= women)
        if form.is_valid():
            form.save()
        return redirect("http://127.0.0.1:8000/women/progression/")

def progressiondetail(request):
    if request.method == "POST":
        formp = ProgressionForm(request.POST,request.FILES)
        if formp.is_valid():
            try:
                formp.save()
                formp = Form()
                #return redirect()
            except:
                pass
    else:
        formp = ProgressionForm() 
    return render(request,"women/progress.html", {'formp':formp})

def progressionshow(request):
    if request.method == "POST":
        locationp = request.POST.get('locationp')
        le = Progression.objects.filter(locationp = locationp)
        return render(request,"women/taskprogress.html",{'le':le})
    else:
        return render(request,"women/search.html",{})




