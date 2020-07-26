from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/login')
    else:
        form = UserRegisterForm()
    return render(request, 'home/signup.html', {'form': form})



def homepage(request):

    return render(request,"home/homepage.html")

def login_success(request):

    rights=request.user.is_staff

    if rights==1:

        return redirect("/admin/task")

    else:

        return redirect("/women")
        