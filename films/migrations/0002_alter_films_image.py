# Generated by Django 3.2.9 on 2021-11-21 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='films_pic'),
        ),
    ]