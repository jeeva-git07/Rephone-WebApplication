from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model=Listing
        fields={'brand','price','ram','model','camera','battery','processor','description','image'}