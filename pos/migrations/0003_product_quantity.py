# Generated by Django 4.0.2 on 2022-02-25 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0002_alter_product_surface'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.FloatField(null=True),
        ),
    ]
