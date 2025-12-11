from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('getaadhar',views.getaadhar,name='getaadhar'),
    path('getpan',views.getpan,name='getpan'),
    path('dlaadhar',views.dlaadhar,name='dlaadhar'),
    path('maskaadhar',views.maskaadhar,name='maskaadhar'),
    path('unmaskaadhar',views.unmaskaadhar,name='unmaskaadhar'),
    path('verifyaadhar',views.verifyaadhar,name='verifyaadhar'),
    path('otp',views.otp,name='otp'),
]

