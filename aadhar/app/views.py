from django.shortcuts import render,redirect
from .models import AadharDetails
from .forms import AadharInfo
from django.core.mail import send_mail
from django.conf import settings
from random import randint
import qrcode

# Create your views here.
def home(request):
    return render(request,'home.html')

def getaadhar(request):
    return render(request,'getaadhar.html')

def getpan(request):
    return render(request,'getpan.html')

def dlaadhar(request):
    return render(request,'dlaadhar.html')

def otp(request):
    msg=""
    notp = int(request.session['otp'])
    if request.method=="POST":
        otp = int(request.POST.get('otp'))
        if notp == otp:
            msg = "otp valid"
            print("success")
            return redirect("dlaadhar")
        else:
            msg = "invalid otp"
            print("failed")
        # return redirect(")

    return render(request,"otp.html",{"msg":msg})

def verifyaadhar(request):
    if request.method=='POST':
        aadharnumber = request.POST.get("aadharnumber")
        request.session['aadharnumber'] = aadharnumber
        data = AadharDetails.objects.get(Aadhar_number = aadharnumber)
        otp = randint(100000,999999)
        request.session['otp'] = otp
        send_mail("OTP GENERATION ",f"Your OTP is {otp} please share it with us to download the aadhar" ,settings.EMAIL_HOST_USER,[data.mail],fail_silently=False)
        return redirect("otp")

    return render(request,"verifyaadhar.html")

def maskaadhar(request):
    aadharnumber = request.session.get('aadharnumber')
    context = {}
    if aadharnumber:
        try:
            data = AadharDetails.objects.get(Aadhar_number=aadharnumber)
            context = {
                'data': data
            }
            # print(data)   # For debugging
        except AadharDetails.DoesNotExist:
            context = {
                'error': "No Aadhaar found for this number."
            }
    else:
        context = {
            'error': "Aadhaar number not found in session."
        }
    return render(request, 'maskaadhar.html', context)

def unmaskaadhar(request):
    aadharnumber = request.session.get('aadharnumber')
    context = {}
    if aadharnumber:
        try:
            data = AadharDetails.objects.get(Aadhar_number=aadharnumber)
            context = {
                'data': data
            }
            # print(data)   # For debugging
        except AadharDetails.DoesNotExist:
            context = {
                'error': "No Aadhaar found for this number."
            }
    else:
        context = {
            'error': "Aadhaar number not found in session."
        }
    return render(request,'unmaskaadhar.html',context)

def register(request):
    form = AadharInfo()
    if request.method=="POST":
        form = AadharInfo(request.POST,request.FILES)
        if form.is_valid():
            phone=form.cleaned_data['phone']
            form.save()
            data = AadharDetails.objects.get(phone=phone)
            send_mail("YOUR AADHAR DETAILS",f"THIS IS YOUR AADHAR NUMBER {data.Aadhar_number} \n PLEASE DOWNLOAD THE COPY OF YOUR  AADHAR FROM OUR WEBSITE ONLY ",settings.EMAIL_HOST_USER,[data.mail],fail_silently=False)
            # print("SUCCESS")
            create_qr(str(data.Aadhar_number),data.first_name,data.address)
    return render(request,"register.html",{'form':form})

def create_qr(aadhar_number, name, address):
    """
    Generate a QR code for Aadhaar with number, name, and address.
    Saves it in media/qrcodes/ (folder must already exist).
    """
    # Prepare data to encode
    data = f"Aadhaar Number: {aadhar_number}\nName: {name}\nAddress: {address}"
    # File path (folder must already exist)
    file_path = f"media/qrcodes/{aadhar_number}.png"
    # Generate QR
    img = qrcode.make(data)
    # Save image
    img.save(file_path)
    print(f"QR code saved at: {file_path}")


# def create_qr(aadhar_number):
#     """
#     Simple function to create a QR code and save with Aadhaar number as filename
#     """
#     img = qrcode.make(aadhar_number)   # generate QR
#     img.save(f"media/qrcodes/{aadhar_number}.png")   # save as <aadhar_number>.png

# def generate_qr(request):
#     aadharnumber = request.session.get('aadharnumber')
#     data = AadharDetails.objects.get(Aadhar_number=aadharnumber)
    
#     # Call the QR function
#     create_qr(aadharnumber)

#     context = {
#         'data': data
#     }
#     return render(request, 'show_aadhar.html', context)
