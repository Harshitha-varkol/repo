from django import forms
from .models import AadharDetails,Gender,State


class AadharInfo(forms.ModelForm):
    gender = forms.ModelChoiceField(
        queryset=Gender.objects.all(),
        empty_label="--SELECT--"
    )
    state = forms.ModelChoiceField(
        queryset=State.objects.all(),
        empty_label="--SELECT--"
    )
    class Meta:
        model=AadharDetails
        fields="__all__"
    
