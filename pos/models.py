from itertools import product
from statistics import mode
from django.db import models

# Create your models here.
class Product(models.Model):


    # mat i sjaj
    surfaces = [
        ('mat', 'Мат'),
        ('sjaj', 'Сјај'),
    ]
    product_types = [
        ('tiles', 'Плочки'),
        ('laminat', 'Ламинат')

    ]


    name = models.CharField(max_length=50, unique=True, null=False)
    manufacturer = models.CharField(max_length=50, null=True)
    # TODO: 
    # date created
    # date updated
    product_type = models.CharField(max_length=10, choices=product_types)
    series = models.CharField(max_length=50, null=False)
    quantity = models.FloatField(null=True)
    price = models.IntegerField(null=True)
    dimensions = models.CharField(max_length=10, null=False)
    surface = models.CharField(max_length=50, choices=surfaces, null=True)
    qunatity_pack = models.FloatField(null=True)
    area_pack = models.FloatField()
    area_pallet = models.FloatField(null=True)

    class Meta:
        db_table = 'Products'
