from django.contrib import admin
from .models import Product, Material, ProductMaterials, Warehouse


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_id')


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductMaterialsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'material_name', 'quantity')


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('material_id', 'remainder', 'price')


admin.site.register(Product, ProductAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(ProductMaterials, ProductMaterialsAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
