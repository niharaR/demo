# Generated by Django 4.1.5 on 2023-02-05 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0004_alter_movie_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='img',
            field=models.ImageField(upload_to='gallery/pic1.jpeg'),
        ),
    ]