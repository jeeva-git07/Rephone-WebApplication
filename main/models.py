from django.db import models
import uuid
from users.models import Profile,Location
from .conts import MOBILE_BRANDS,RAM
from .utils import user_listing_path

class Listing(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True,editable=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    seller=models.ForeignKey(Profile,on_delete=models.CASCADE)
    price=models.IntegerField(default=0)
    brand=models.CharField(max_length=24,choices=MOBILE_BRANDS,null=False)
    ram=models.CharField(max_length=10,choices=RAM)
    model=models.CharField(max_length=10)
    camera=models.CharField(max_length=30,default="0 Mp")
    battery=models.CharField(max_length=24,default="0 mah")
    processor=models.CharField(max_length=24,default="Enter Processor here")
    description=models.TextField()
    location=models.OneToOneField(Location,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=user_listing_path)

    def __str__(self):
        return f"{self.seller.user.username}--{self.brand}"