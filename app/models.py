from distutils.command.upload import upload
import email
from django.db import models

# Create your models here.

class Events(models.Model):
    event=models.CharField(max_length=60)
    member= models.CharField(max_length=50)
    start= models.DateTimeField()
    end= models.DateTimeField()
    location=models.CharField(max_length=60)
    profile=models.ImageField(upload_to="images/", max_length=300, null=True, default=None)

    def __str__(self):
        return self.event


gender=(
    ('Male','Male'),
    ('Female','Female'),

)


class RegisterAdmin(models.Model):
    username=models.CharField(max_length=30)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    pass1=models.CharField(max_length=20)
    pass2=models.CharField(max_length=20)
    gender=models.CharField(max_length=8,choices=gender,default="")


    def __str__(self):
        return self.username


class RegisterUser(models.Model):
    username=models.CharField(max_length=30)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    pass1=models.CharField(max_length=20)
    pass2=models.CharField(max_length=20)
    gender=models.CharField(max_length=8,choices=gender,default="")


    def __str__(self):
        return self.username