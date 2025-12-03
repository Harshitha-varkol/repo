from django.shortcuts import render
from .models import Student


# Create your views here.
def home(request):
    data=Student.objects.all()
    context={
        'data':data
    }
    return render(request,'home.html',context)

