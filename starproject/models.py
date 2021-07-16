from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile",primary_key=True)
    profile_picture = CloudinaryField('image')
    bio= models.TextField()
    contact = models.CharField(max_length=60,blank=True)
    



class Project(models.Model):
    title = models.CharField(max_length=60,blank=True)
    image = CloudinaryField('image')
    description = models.TextField()
    link = models.URLField(blank=True)
    profile = models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)
   