from django.shortcuts import render

# Create your views here.
def loginpage(request):
    return render(request,'login.html')

def mainpage(request):
    return render(request,'mainpage.html')

def support(request):
    return render(request,'support.html')

def premium(request):
    return render(request,'premium.html')

def download(request):
    return render(request,'download.html')

def signup(request):
    return render(request,'signup.html')

