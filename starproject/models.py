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




class Review(models.Model):
    ratings= (
        (1, '1'),(2, '2'),
        (3, '3'),(4, '4'),
        (5, '5'),(6, '6'),
        (7, '7'),(8, '8'),
        (9, '9'),(10, '10'),
    )
    user = models.ForeignKey(User,null=True,blank=True)
    content = models.IntegerField(choices=ratings,blank=False,default=0)
    design = models.IntegerField(choices=ratings,default=0,blank=False)
    usability = models.IntegerField(choices=ratings,blank=False,default=0)
    project = models.ForeignKey(Project,null=True,on_delete=models.CASCADE)
    average =  models.DecimalField(default=1,blank=False,max_digits=30,decimal_places=2)
   
