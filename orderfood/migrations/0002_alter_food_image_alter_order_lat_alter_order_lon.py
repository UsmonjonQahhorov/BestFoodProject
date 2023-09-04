# Generated by Django 4.2.4 on 2023-09-04 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderfood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(upload_to='media/food_images/'),
        ),
        migrations.AlterField(
            model_name='order',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='lon',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
    ]
