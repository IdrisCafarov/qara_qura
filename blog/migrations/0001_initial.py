# Generated by Django 4.1.2 on 2022-11-21 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_1', models.CharField(max_length=150, null=True, verbose_name='Title 1')),
                ('title_2', models.CharField(max_length=150, null=True, verbose_name='Title 2')),
            ],
        ),
        migrations.CreateModel(
            name='AboutHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100, verbose_name='Header')),
                ('content', models.TextField(verbose_name='Content')),
            ],
        ),
        migrations.CreateModel(
            name='AboutHeader_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100, verbose_name='Header')),
                ('content', models.TextField(verbose_name='Content')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Name')),
                ('surname', models.CharField(max_length=25, null=True, verbose_name='Surname')),
                ('number', models.CharField(max_length=20, null=True, verbose_name='Number')),
                ('email', models.EmailField(max_length=30, verbose_name='Email')),
                ('text', models.TextField(verbose_name='Message')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(upload_to='Logo')),
                ('header_text', models.TextField()),
                ('footer_1', models.CharField(max_length=50)),
                ('footer_2', models.CharField(max_length=50)),
                ('footer_3', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('surname', models.CharField(max_length=100, verbose_name='Surname')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
                ('image', models.ImageField(upload_to='Instructors')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='Images', verbose_name='Add Image')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('draft', models.BooleanField(default=False, verbose_name='Show')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(upload_to='Images', verbose_name='Add Image')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='Images', verbose_name='Add Image')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='Images', verbose_name='Add Image')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='Images', verbose_name='Add Image')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solution', to='blog.product')),
            ],
        ),
    ]