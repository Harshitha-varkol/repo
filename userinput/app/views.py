from django.shortcuts import render,HttpResponse

# Create your views here.
def input(request):
    if request.method=='POST':
        username=request.POST.get('un')
        password=request.POST.get('pswd')
        copassword=request.POST.get('cpswd')
        # print(username)
        # print(password)
        # print(copassword)
        if password==copassword:
            if username=='harshitha' and password=='harsh@123':
                return HttpResponse('login successful')
            else:
                return HttpResponse('invalid credentials')
        else:
            return HttpResponse('password mismatch')    
    
    return render(request,'index.html')

def calci(request):
    if request.method=="POST":
        num1=int(request.POST.get('num1'))
        num2=int(request.POST.get('num2'))
        a=request.POST.get('operation')
        if a=="ADD":
            return HttpResponse(f"the addition of {num1} and {num2} is {num1+num2}")
        elif a=="SUB":
            return HttpResponse(f"the subtraction of {num1} and {num2} is {num1-num2}")
        elif a=="MUL":
            return HttpResponse(f"the multiplication of {num1} and {num2} is {num1*num2}")
        elif a=="DIV":
            return HttpResponse(f"the division of {num1} and {num2} is {num1/num2}")

        
    return render(request,'calculator.html')
