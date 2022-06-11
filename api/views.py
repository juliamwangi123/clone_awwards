from pickle import NONE
from django.shortcuts import redirect, render
from .forms import regUserForm
from django.contrib.auth import authenticate, login
# Create your views here.
def home(req):
    return  render (req, 'api/home.html')

def regUser(req):
    form=regUserForm()
    if req.method == 'POST':
        form=regUserForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=regUserForm(req.POST) 

    return render (req, 'api/reg.html' , {'form':form})



def loginUser(req):
    if req.method =='POST':
        username=req.POST.get('username')
        password=req.POST.get('password')
        user=authenticate(username=username , password=password)
        print(password)
        if user is not None:
            login(req, user)
            return redirect('home')


    return render(req, 'api/login.html')


def userProfile(req):
    return render (req, 'api/profile.html')
    
