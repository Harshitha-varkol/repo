from django.shortcuts import render , HttpResponse , redirect
from .models import Account
from django.core.mail import send_mail
from django.conf import settings
from random import randint
from django.contrib import messages
import  hashlib 
import time 
from decimal import Decimal as de
# Create your views here.
def index(request):
    return render(request,'index.html')

def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        mail = request.POST.get("mail")
        add = request.POST.get("add")
        gen = request.POST.get("gen")
        date = request.POST.get("date")
        aaddhar = request.POST.get("aadhar")

        if Account.objects.filter(email=mail).exists():
            messages.error(request, "This email is already registered.")
            return render(request, "create.html")

        acc = Account.objects.create(
            name=name, phone=phone, email=mail,
            address=add, aadhar=aaddhar, dob=date, gender=gen
        )

        send_mail(
            "Account created successfully",
            f"Your account number is {acc.account_num}. Enjoy our services!",
            settings.EMAIL_HOST_USER, [acc.email], fail_silently=False
        )

        messages.success(request, "Account created successfully ✅")
        return render(request, "create.html")

    return render(request, "create.html")



def cash_withdraw(request):
    msg = ""
    
    if request.method == "POST":
        acc = int(request.POST.get('acc'))
        pin = request.POST.get('pin')
        amt = de(request.POST.get('amt'))  
        
        data = Account.objects.get(account_num=acc)
        npin = encrypt(str(pin))
        
        if data.pin == npin:
            if amt > de("100"):
                if amt <= de("10000"):
                    data.balance -= amt
                    data.save()
                    send_mail(
                        "WITHDRAW",
                        f"mi bank account lo nunchi aksharala {amt} rs sai ram\nthank you boss\nlove you bache",
                        settings.EMAIL_HOST_USER,
                        [data.email],
                        fail_silently=False
                    )
                    return redirect("home")
                else:
                    msg = "amt is aukat ke bahar"
            else:
                msg = "amt should be greater than 500"
        

    return render(request,'cashwithdraw.html')

def deposite(request):
    msg = ""
    if request.method == "POST":
        acc = request.POST.get('acc')
        pin = request.POST.get('pin')
        amt = int(request.POST.get('amt'))
        try:
            data = Account.objects.get(account_num = acc)
        except Exception as e:
            msg = e
        if data:
            npin = encrypt(str(pin))
            if data.pin == npin:
                if amt>100:
                    if amt<=10000:
                        data.balance += amt
                        data.save()
                        send_mail("DEPOSIT",f"mi bank account loki aksharala  {amt} rs vachi padayi \n thank you boss \n love you bache " ,settings.EMAIL_HOST_USER,[data.email],fail_silently=False)
                        return redirect("home")
                    else:
                        msg = "amt is aukat ke bahar"
                else:
                    msg = "amt should be greater than 500"
    return render(request,'deposite.html',{"msg":msg})

def pincode(request):
    if request.method == "POST":
        acc = request.POST.get("acc")
        data = Account.objects.get(account_num = acc)
        otp = randint(100000,999999)
        # print(otp)
        request.session['otp'] = otp
        send_mail("PIN GENERATION ",f"ur one time password is {otp} please share it with our scamers only" ,settings.EMAIL_HOST_USER,[data.email],fail_silently=False)
        return redirect('otp')
    return render(request,'pincode.html')

def transfer(request):
    form = True
    balance = None
    error = None
    from_acc = ""   # initialize
    pin = ""        # initialize

    if request.method == "POST":
        from_acc = request.POST.get("fromacc", "")
        pin = request.POST.get("pin", "")
        to_acc = request.POST.get("toacc")
        amount = request.POST.get("amt")

        # FIRST FORM: checking sender account and PIN
        if not to_acc and not amount:
            try:
                account = Account.objects.get(account_num=from_acc)
            except Account.DoesNotExist:
                error = "Account not found"
            else:
                encrypted_pin = encrypt(str(pin))
                if account.pin == encrypted_pin:
                    form = False
                    balance = account.balance
                else:
                    error = "Invalid PIN"

        # SECOND FORM: performing transfer
        else:
            try:
                sender = Account.objects.get(account_num=from_acc)
                receiver = Account.objects.get(account_num=to_acc)
            except Account.DoesNotExist:
                error = "Sender or Receiver account not found"
            else:
                encrypted_pin = encrypt(str(pin))
                if sender.pin != encrypted_pin:
                    error = "Invalid PIN"
                elif int(amount) > sender.balance:
                    error = "Insufficient balance"
                else:
                    sender.balance -= int(amount)
                    receiver.balance += int(amount)
                    sender.save()
                    receiver.save()
                    balance = sender.balance
                    form = False
                    error = f"Successfully transferred {amount} to {to_acc}"
                    send_mail(
                        "TRANSFER",
                        f"₹{amount} has been credited to your account. Thank you!",
                        settings.EMAIL_HOST_USER,
                        [receiver.email],  # use receiver object
                        fail_silently=False
                    )
                    return transfer_success(request, amount, to_acc)

    context = {
        "form": form,
        "balance": balance,
        "fromacc": from_acc,
        "pin": pin,
        "error": error,
    }
    return render(request, "transfer.html", context)


from django.http import HttpResponse

def transfer_success(request, amount, toacc):
    html_content = f"""
    <html>
        <head>
            <title>Transfer Success</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin-top: 50px;
                    background-color: #f0f0f0;
                }}
                .button {{
                    padding: 10px 20px;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 16px;
                    text-decoration: none;
                }}
                .button:hover {{
                    background-color: #45a049;
                }}
            </style>
        </head>
        <body>
            <h1>Transfer Successful!</h1>
            <p>₹{amount} has been transferred to account {toacc}.</p>
            <a href="/" class="button">Return to Home</a>
        </body>
    </html>
    """
    return HttpResponse(html_content)


def user(request):
    if request.method == "POST":
        a = Account.objects.get(account_num = request.POST.get('acc'))
        a.delete()
        return redirect("home")
    return render(request,'user.html')

def encrypt(data):
    return hashlib.shake_256(data.encode()).hexdigest(length=32)
def wallet(request):
    msg = ""
    if request.method == "POST":
        acc = request.POST.get('acc')
        pin = request.POST.get('pin')
        try:
            data = Account.objects.get(account_num = acc)
        except Exception as e:
            msg = e
        if data:
            npin = encrypt(str(pin))
            if data.pin == npin:
                msg = data.balance
                return redirect("home")
            else:
                msg = "pin is in correct"

        time.sleep(5)
    return render(request,'wallet.html',{'msg':msg})
    




def otp_validation(request):
    msg = ""
    late_otp = request.session['otp']
    if request.method == "POST":
        phone = int(request.POST.get('mobile'))
        notp = int(request.POST.get('notp'))
        cotp = int(request.POST.get('cotp'))
        npin = int(request.POST.get('npin'))
        cpin = int(request.POST.get('cpin'))
        # print(phone,notp,npin,cotp,cpin)
        if notp == cotp:
            if npin == cpin:
                data = Account.objects.get(phone = phone)
                # data.pin = npin
                data.pin = encrypt(str(npin))
                data.save()
                msg = "pin genrated successfully"
                send_mail("PIN GENERATED SUCCESSFULLY ","the pin has been generated and set to ur account please don't x=share it with other scamers only share with us \n thank you \n love you bache \n regards \n ibmc manager",settings.EMAIL_HOST_USER,[data.email],fail_silently=False)
            else:
                msg = "pin mismatch"
        else:
            msg = "otp mismatch"
    return render(request,"otp_validation.html",{"msg":msg})



# xaee tgxc cqlw cyko