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
    name = models.CharField(max_length=100,null=True, blank=True)
    surname = models.CharField(max_length=100,null=True, blank=True)
    social_link = models.TextField(null=True, blank=True)
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
    name = models.CharField(max_length=100,null=True, blank=True)
    surname = models.CharField(max_length=100,null=True, blank=True)
    social_link = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product",null=True,blank=True)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    show = models.BooleanField(default=False,verbose_name="Show")
    description = RichTextField(verbose_name="Description",null=True,blank=True)


    # def __str__(self):
    #     return "solution for "+ str(self.product.id)

from django_base64field.fields import Base64Field
from django.core.exceptions import ValidationError



#################### base 64 decoder ########################
from django.core.files.base import ContentFile
import uuid

import base64
import os

from django.conf import settings


def image_as_base64(image_file, format='png'):
    """
    :param `image_file` for the complete path of image.
    :param `format` is format for image, eg: `png` or `jpg`.
    """
    if not os.path.isfile(image_file):
        return None

    encoded_string = ''
    with open(image_file, 'rb') as img_f:
        encoded_string = base64.b64encode(img_f.read())
    return 'data:image/%s;base64,%s' % (format, encoded_string)

#########################################################





class Portfolio(models.Model):

    name = models.CharField(max_length=100)
    image = models.FileField(upload_to="Ravan_pp")

    positon =  models.CharField(max_length=100, null=True, blank=True)

    mail = models.CharField(max_length=500,null=True,blank=True)
    adress = models.CharField(max_length=100, null=True,blank=True)

    linkedin = models.CharField(max_length=500,null=True,blank=True)
    github = models.CharField(max_length=500,null=True,blank=True)
    whatsapp = models.CharField(max_length=500,null=True,blank=True)
    instagram = models.CharField(max_length=500,null=True,blank=True)
    facebook = models.CharField(max_length=500,null=True,blank=True)

    ####

    page_title = models.CharField(max_length=300)
    title_about = models.CharField(max_length=300)
    experience_year = models.PositiveIntegerField(default=1)
    projects_count = models.PositiveIntegerField(default=1)

    ######
    about_title = models.CharField(max_length=300)
    about_main = models.TextField()

    def __str__(self):
        return self.name



    # def clean(self):
    #     if Portfolio.objects.exists() and not self.pk:
    #         raise ValidationError("You can only have one company")


    # def save(self, *args, **kwargs):
    #    return super(Portfolio, self).save(*args, **kwargs) #saves the record




class Education(models.Model):
    user_port = models.ForeignKey(Portfolio,on_delete=models.CASCADE, related_name="education")
    title = models.CharField(max_length=300)
    place = models.CharField(max_length=300)
    start_year = models.CharField(max_length=100)
    end_year = models.CharField(max_length=100)

class Experience(models.Model):
    user_port = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="experience")
    title = models.CharField(max_length=300)
    place = models.CharField(max_length=300)
    start_year = models.CharField(max_length=100)
    end_year = models.CharField(max_length=100)


class Specialization(models.Model):
    user_port = models.ForeignKey(Portfolio,on_delete=models.CASCADE, related_name="specialization")
    title = models.CharField(max_length=100)
    about = models.CharField(max_length=200)
    count = models.PositiveIntegerField(default=0)

class Skills(models.Model):
    user_port = models.ForeignKey(Portfolio,on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to="Skills")





class Project(models.Model):
    user = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="projects")
    name = models.CharField(max_length=100)
    main_title = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='ProjectImages')
    video_link = models.CharField(max_length=10000, null=True)
    url = models.CharField(max_length=500)
    text = models.TextField()

    def __str__(self):
        return self.name

class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.FileField(upload_to="ProjectImages")


class Technologies(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="technology")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name












