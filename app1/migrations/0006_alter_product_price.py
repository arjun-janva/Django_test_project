# Generated by Django 4.1.4 on 2023-08-03 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_product_description_product_price_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Price',
            field=models.IntegerField(default=0),
        ),
    ]
