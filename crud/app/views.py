from django.shortcuts import render,redirect
from .models import Registration
# Create your views here.
def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        branch=request.POST.get('branch')
        marks=request.POST.get('marks')
        age=request.POST.get('age')
        address=request.POST.get('address')
        user=Registration.objects.create(name=name,branch=branch,marks=marks,age=age,address=address)
        return redirect('success',user_id=user.id)
    return render (request,'registration.html')

def success(request,user_id):
    return render(request,'success.html',{'user_id':user_id})

def view_details(request,user_id):
    user=Registration.objects.get(id=user_id)
    return render(request,'view.html',{'user':user})

def edit(request,user_id):
    user=Registration.objects.get(id=user_id)
    context={
        'user':user
    }
    if request.method=="POST":
        name=request.POST.get('name')
        branch=request.POST.get('branch')
        marks=request.POST.get('marks')
        age=request.POST.get('age')
        address=request.POST.get('address')
        user.name=name
        user.branch=branch
        user.marks=marks
        user.age=age
        user.address=address
        user.save()
        return redirect('view',user_id=user.id)
    return render(request,'edit.html',context)


