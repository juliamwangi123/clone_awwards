from django.shortcuts import redirect, render
from .forms import regUserForm
from django.contrib.auth import authenticate, login
from rest_framework.decorators import  api_view
from rest_framework.response import Response
from .models import Site
from .serializer import SiteSerializer
from urllib import request, response
import json
from django.views.generic import DetailView
from .models  import Site
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.


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


def logoutUser(req):
    logout(req)
    return redirect('home')

def userProfile(req):
    data=Site.objects.filter(owner=req.user)
    return render (req, 'api/profile.html', {'datas':data})
    

@api_view(['GET'])
def api(req):
    if req.method=='GET':
        site=Site.objects.all()
        serializedSite=SiteSerializer(site , many=True)
        return Response(serializedSite.data)

def home(req):
    url='http://127.0.0.1:8000/sites'
    response=request.urlopen(url)
    result=response.read()
    data=json.loads(result)
    top=data[2]
    context={
        'top':top,
        'datas':data
    }

    
    return render(req, 'api/home.html' , context)


def submit_site(req):
    if req.method == "POST" :
        name=req.POST.get('name')
        url=req.POST.get('url')
        image=req.FILES['image']
        site= Site(owner=req.user, image=image, url=url, name=name)
        print(image)
        site.save()
        return redirect('home')
        
    return render (req, 'api/submit.html')



class SiteDetailView(DetailView):
    model=Site
    context_object_name='site'








