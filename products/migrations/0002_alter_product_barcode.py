# Generated by Django 4.2.3 on 2023-07-05 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='barcode',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
