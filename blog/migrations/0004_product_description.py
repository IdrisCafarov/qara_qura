# Generated by Django 4.1.2 on 2022-10-31 12:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Description'),
        ),
    ]
