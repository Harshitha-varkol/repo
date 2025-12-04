from django.shortcuts import render,redirect
from .forms import Employee_form
# Create your views here.

def form(request):
    if request.method=="POST":
        form_instance = Employee_form(request.POST)
        if form_instance.is_valid():
            form_instance.save() 
            return redirect('success') 
    else:
        form_instance = Employee_form()

    return render(request,'from.html',{'form':form_instance})

def success(request):
    return render(request,'success.html')