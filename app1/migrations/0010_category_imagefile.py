# Generated by Django 4.1.4 on 2023-08-09 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_product_imagefile'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='ImageFile',
            field=models.ImageField(blank=True, upload_to='category_image'),
        ),
    ]
