from django.db import models
from .consts import DISTRICTS_LIST,STATES_LIST
from django.contrib.auth.models import User

class Location(models.Model):
    address1=models.CharField(max_length=140,blank=True)
    address2=models.CharField(max_length=140,blank=True)
    city=models.CharField(max_length=50,choices=DISTRICTS_LIST)
    state=models.CharField(max_length=50,choices=STATES_LIST)
    pincode=models.CharField(max_length=10,blank=True)

    def __str__(self):
        return f'Location {self.id}'
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.CharField(max_length=250,blank=True)
    phone_number=models.CharField(max_length=10,blank=True)
    location=models.OneToOneField(Location,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"