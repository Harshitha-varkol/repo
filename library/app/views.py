from django.shortcuts import render,redirect
from . models import Library
# Create your views here.
def library(request):
    if request.method=='POST':
        name=request.POST.get('name')
        author=request.POST.get('name')
        genre=request.POST.get('genre')
        price=request.POST.get('price')
        available=request.POST.get('available')
        lib=Library.objects.create(
            name=name,
            author=author,
            genre=genre,
            price=price,
            available=available,
        )
        return redirect('success')
    return render(request,'index.html')

def list(request):
    books=Library.objects.all()
    return render(request,'list.html',{'books':books})

def show(request):
    books=Library.objects.all()
    return render(request,'show.html',{'books':books})

def edit(request, id):
    lib = Library.objects.get(id=id)
    if request.method == 'POST':
        lib.name = request.POST.get('name')
        lib.author = request.POST.get('author')
        lib.genre = request.POST.get('genre')
        lib.price = request.POST.get('price')
        lib.available = request.POST.get('available')
        lib.save()
        return redirect('display_books')
    return render(request, 'edit.html', {'book': lib})

def success(request):
    return render(request,'success.html')