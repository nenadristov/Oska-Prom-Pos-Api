# Generated by Django 4.0.2 on 2022-03-05 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0005_alter_product_area_pallet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(max_length=50, null=True),
        ),
    ]