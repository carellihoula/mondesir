# Generated by Django 3.2.9 on 2021-11-26 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_alter_films_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='image',
            field=models.ImageField(upload_to='films_pic'),
        ),
    ]
