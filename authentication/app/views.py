from django.shortcuts import render
from .forms import Registerform,Captcha

# Create your views here.

def register(request):
    form=Registerform()
    form1=Captcha()
    context={
        'form':form,
        'form1':form1
    }
    if request.method=="POST":
        form=Registerform(request.POST)
        form1=Captcha(request.POST)
        if form.is_valid() and form1.is_valid():
            form.save()
    return render(request,'register.html',context)
