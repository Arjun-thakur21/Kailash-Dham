from django.db import models
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField 


class Contact(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField( max_length=50)
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=100)

class Service(models.Model):
    Service_icon=models.CharField(max_length=100)
    Service_title=models.CharField(max_length=50)
    Service_decs=RichTextField()

    def __str__(self):
        return self.Service_title

class Rating(models.Model):
    Rating_title=models.CharField(max_length=50)
    Rating_decs=RichTextField()
    Rating_image=models.ImageField(upload_to="rating/", max_length=250,null=True,default=None)
    Rating_about=models.CharField(max_length=50,default="")

class Agents(models.Model):
    Agents_name = models.CharField(max_length=50)
    Agents_desc1 = RichTextField()
    Agents_image = models.ImageField(upload_to="Agents/", max_length=250, null=True, default=None)
    Agents_phone = PhoneNumberField(blank=True, null=True) 

    def __str__(self):
        return self.Agents_name


class Properties(models.Model):
    agent = models.ForeignKey(Agents, on_delete=models.CASCADE, related_name='Properties',null=True)
    Properties_name=models.CharField(max_length=50)
    Properties_address=models.TextField()
    Properties_price =models.CharField(max_length=20, null=True )
    Properties_image=models.ImageField(upload_to="Properties/",max_length=500,null=True,default=None)
    Properties_image1=models.ImageField(upload_to="sub/",max_length=250,null=True,default=None)
    Properties_image2=models.ImageField(upload_to="sub/",max_length=250,null=True,default=None)
    Properties_image3=models.ImageField(upload_to="sub/",max_length=250,null=True,default=None)
    Properties_desc=RichTextField(default=())

class About(models.Model):
    About_icone=models.CharField(max_length=100)
    About_name=models.CharField(max_length=50)
    About_desc1=RichTextField()
    About_image=models.ImageField(upload_to="about/",max_length=250,null=True,default=None)
    About_Us1=RichTextField(default=())
    About_Us2=RichTextField(default=())
   
class Team(models.Model):
    Team_name=models.CharField(max_length=50)
    Team_desc=RichTextField()
    Team_rank=models.CharField(max_length=100)
    Team_image=models.ImageField(upload_to="team/",max_length=500,null=True,default=None)
    Team_phone=PhoneNumberField(null=True, blank=True)

class Image(models.Model):
    Image_name=models.CharField(max_length=50)
    Images=models.ImageField(upload_to="image/",max_length=250,null=True,default=None)