# Generated by Django 4.1.3 on 2022-12-14 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_products_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='available',
            field=models.BooleanField(),
        ),
    ]
