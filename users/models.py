from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Address(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    street=models.CharField(max_length=50,default="")
    city=models.CharField(max_length=50,default="")
    state=models.CharField(max_length=50,default="")
    zip=models.CharField(max_length=50,default="")

    def __str__(self) :
        return str(self.user)

class Profile(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    image =models.ImageField(default='photos/23/05/21/default-icon.png',upload_to='photos/profile_pics/')
    phone=models.CharField(max_length=50,default="", null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
