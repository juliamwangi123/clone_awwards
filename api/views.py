from django.shortcuts import redirect, render
from .forms import regUserForm

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


