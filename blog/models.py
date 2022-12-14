from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class GeneralSettings(models.Model):
    logo = models.FileField(upload_to="Logo")
    header_text = RichTextField()
    instagram = models.CharField(max_length=50,null=True,blank=True)
    linkedin = models.CharField(max_length=50,null=True,blank=True)
    facebook = models.CharField(max_length=50,null=True,blank=True)

    class Meta:
        verbose_name = "General Settings"
        verbose_name_plural = "General Settings"




class Product(models.Model):
    image = models.ImageField(upload_to="Images",verbose_name="Add Image",null=True)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    turn = models.PositiveIntegerField(default=0)
    description = RichTextField(verbose_name="Description",null=True,blank=True)
    draft = models.BooleanField(verbose_name="Show",default=False)
    problem = RichTextField(null=True,blank=True)
    solution_text = RichTextField(null=True,blank=True)
    

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Galeries"
        verbose_name_plural = "Galeries"

        
    

class About(models.Model):
    title_1_little = RichTextField(verbose_name="Tittle 1 Little",null=True,blank=True)
    title_1 = RichTextField(verbose_name="Title 1",null=True,blank=True)
    title_2 = RichTextField(verbose_name="Title 2",null=True,blank=True)

    def __str__(self):
        return "About"

    class Meta:
        verbose_name = "About Title"
        verbose_name_plural = "About Titles"
    



class Contact(models.Model):
    name = models.CharField(max_length=25,verbose_name="Name")
    surname = models.CharField(max_length=25,verbose_name="Surname",null=True)
    number = models.CharField(max_length=20,verbose_name="Number",null=True)
    email = models.EmailField(max_length=30,verbose_name="Email")
    text = RichTextField(verbose_name="Message")

    def __str__(self):
        return self.email



class AboutHeader(models.Model):
    header = RichTextField(max_length=100,verbose_name="Header")
    content = RichTextField(verbose_name="Content")
    # little_header = models.TextField(null=True)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = "About Content"
        verbose_name_plural = "About Contents"
    

class AboutHeader_2(models.Model):
    header = RichTextField(max_length=100,verbose_name="Header")
    content = RichTextField(verbose_name="Content")

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = "About Content 2"
        verbose_name_plural = "About Contents 2"


class Instructor(models.Model):
    name = models.CharField(max_length=100,verbose_name="Name")
    surname = models.CharField(max_length=100,verbose_name="Surname")
    position = models.CharField(max_length=100,verbose_name="Position")
    image = models.ImageField(upload_to="Instructors")

    def __str__(self):
        return self.name+' '+self.surname


class Solution(models.Model):
    image = models.ImageField(upload_to="Images",verbose_name="Add Image",null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product",null=True,blank=True)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    show = models.BooleanField(default=False,verbose_name="Show")
    description = RichTextField(verbose_name="Description",null=True,blank=True)


    # def __str__(self):
    #     return "solution for "+ str(self.product.id)
    


    
    

    
    

