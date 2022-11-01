# Generated by Django 4.1.2 on 2022-11-01 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_aboutheader_2'),
    ]

    operations = [
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
    ]
