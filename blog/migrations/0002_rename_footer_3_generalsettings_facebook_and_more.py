# Generated by Django 4.1.2 on 2022-11-21 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generalsettings',
            old_name='footer_3',
            new_name='facebook',
        ),
        migrations.RenameField(
            model_name='generalsettings',
            old_name='footer_1',
            new_name='instagram',
        ),
        migrations.RenameField(
            model_name='generalsettings',
            old_name='footer_2',
            new_name='linkedin',
        ),
    ]