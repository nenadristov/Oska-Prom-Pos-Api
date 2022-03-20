from itertools import product
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):

    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    manufacturer = serializers.CharField()
    product_type = serializers.CharField()
    series = serializers.CharField(required=False)
    surface = serializers.CharField(required=False)
    quantity = serializers.FloatField()
    qunatity_pack = serializers.FloatField(required=False)
    area_pack = serializers.FloatField()
    area_pallet = serializers.FloatField(required=False)
    price = serializers.IntegerField(required=False)
    dimensions = serializers.CharField(required=False)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.product_type = validated_data.get('product_type', instance.product_type)
        instance.series = validated_data.get('series', instance.series)
        instance.surface = validated_data.get('surface', instance.surface)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.qunatity_pack = validated_data.get('qunatity_pack', instance.qunatity_pack)
        instance.area_pack = validated_data.get('area_pack', instance.area_pack)
        instance.area_pallet = validated_data.get('area_pallet', instance.area_pallet)
       


        instance.save()
        return instance


class ProductShortSerializer(serializers.Serializer):

    #id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    """ product_type = serializers.CharField()
    quantity = serializers.FloatField()
    price = serializers.IntegerField()"""
    