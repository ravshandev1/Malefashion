# Generated by Django 3.2.13 on 2022-06-17 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_productcolor_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mid_rate',
            field=models.FloatField(default=0),
        ),
    ]