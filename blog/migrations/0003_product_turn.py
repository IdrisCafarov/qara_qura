# Generated by Django 4.1.2 on 2022-11-25 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_product_turn'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='turn',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
