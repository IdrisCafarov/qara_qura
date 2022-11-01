from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Product(models.Model):
    image = models.ImageField(upload_to="Images",verbose_name="Add Image")
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(verbose_name="Description",null=True,blank=True)
    draft = models.BooleanField(verbose_name="Show",default=False)

    def __str__(self):
        return str(self.id)
    

class About(models.Model):
    title_1 = models.CharField(max_length=150,verbose_name="Title 1")
    title_2 = models.CharField(max_length=150,verbose_name="Title 2")

    def __str__(self):
        return "About"
    



class Contact(models.Model):
    name = models.CharField(max_length=25,verbose_name="Name")
    surname = models.CharField(max_length=25,verbose_name="Surname",null=True)
    number = models.CharField(max_length=20,verbose_name="Number",null=True)
    email = models.EmailField(max_length=30,verbose_name="Email")
    text = models.TextField(verbose_name="Message")

    def __str__(self):
        return self.email



class AboutHeader(models.Model):
    header = models.CharField(max_length=100,verbose_name="Header")
    content = models.TextField(verbose_name="Content")

    def __str__(self):
        return self.header
    

    

