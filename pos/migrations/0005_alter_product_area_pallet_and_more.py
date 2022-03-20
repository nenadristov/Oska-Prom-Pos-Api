# Generated by Django 4.0.2 on 2022-03-03 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0004_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='area_pallet',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='qunatity_pack',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='surface',
            field=models.CharField(choices=[('mat', 'Мат'), ('sjaj', 'Сјај')], max_length=50, null=True),
        ),
    ]
