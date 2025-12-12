from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_recaptcha.fields import ReCaptchaField

class Registerform(UserCreationForm):
    pass
    

class Captcha(forms.Form):
    captcha = ReCaptchaField()