from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdminManager(admin.ModelAdmin):
    list_display = ('name', 'product_type', 'series', 'dimensions', 'surface', 'qunatity_pack', 'area_pack', 'area_pallet')



admin.site.register(Product, ProductAdminManager)