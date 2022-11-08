from django.shortcuts import render
from .forms import UserForm
from .models import User
from django.http import HttpResponseRedirect
from django.contrib import messages

# from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def form(request):
    us=User.objects.all()
    if request.method == "POST":
        uf=UserForm(request.POST)      
        if uf.is_valid():
            un=uf.cleaned_data["username"]
            em=uf.cleaned_data["email"]
            pw=uf.cleaned_data["password"]
            
            uset=User(username=un,email=em,password=pw)
            uset.save()
            uf=UserForm()
            messages.success(request,"Your form has been submitted successfully")
 
    else:
        uf=UserForm()            
    return render(request,"form.html",{"us":us,"uf":uf})        

def delete_data(request,id): 
    if request.method == "POST":  
        us=User.objects.get(pk=id)
        us.delete()
        return HttpResponseRedirect("/form/")

def update_data(request,id):
    if request.method == "POST":
        us=User.objects.get(pk=id)
        uf=UserForm(request.POST,instance=us)
        if uf.is_valid():

            uf.save()
            uf=UserForm()
            return HttpResponseRedirect("/form/")
    else:
       us=User.objects.get(pk=id)
       uf=UserForm(instance=us)          
    return render(request,"form1.html",{"uf":uf}) 

