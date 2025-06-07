from django import forms
from django.contrib.auth.models import User
from .models import Location,Profile

class UserForm(forms.ModelForm):
    username=forms.CharField(disabled=True)
    class Meta:
        model=User
        fields={"username"}

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=("bio","phone_number")


class LocationForm(forms.ModelForm):
    pincode=forms.CharField(required=True)
    address1=forms.CharField(required=True)
    class Meta:
        model=Location
        fields={"address1","address2","city","state","pincode"}