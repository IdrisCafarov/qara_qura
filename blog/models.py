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
    text_1 = RichTextField(verbose_name="Text 1")
    text_2 = RichTextField(verbose_name="Text 1")
    text_3 = RichTextField(verbose_name="Text 1")


    def __str__(self):
        return "About"
    



class Contact(models.Model):
    name = models.CharField(max_length=25,verbose_name="Name")
    email = models.EmailField(max_length=30,verbose_name="Email")
    text = models.TextField(verbose_name="Message")

    def __str__(self):
        return self.email
    

