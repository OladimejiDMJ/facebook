# Generated by Django 2.2.6 on 2019-11-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_uploaded',
            field=models.DateField(default='19-11-29'),
        ),
    ]
