# Generated by Django 4.1.3 on 2022-11-26 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_products'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='catag',
            new_name='categ',
        ),
        migrations.AlterModelOptions(
            name='categ',
            options={'ordering': ['name'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.categ'),
            preserve_default=False,
        ),
    ]
