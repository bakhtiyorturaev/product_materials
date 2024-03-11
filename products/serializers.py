# from rest_framework import serializers
#
# from products.models import Warehouse, ProductMaterials
#
#
# class WarehouseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Warehouse
#         fields = ['id', 'price', 'remainder']
#
#
# class ProductMaterialsSerializer(serializers.ModelSerializer):
#     material_name = serializers.CharField(source='material_name.name')
#
#     class Meta:
#         model = ProductMaterials
#         fields = ['material_name', 'quantity']
#
#
# class ProductResultSerializer(serializers.Serializer):
#     warehouse_id = serializers.IntegerField(allow_null=True)
#     material_name = serializers.CharField()
#     qty = serializers.FloatField(allow_null=True)
#     price = serializers.FloatField(allow_null=True)
#
#
# class ProductMaterialsAPIViewSerializer(serializers.Serializer):
#     product_name = serializers.CharField()
#     product_qty = serializers.IntegerField()
#     product_materials = ProductResultSerializer(many=True)
#
#     def to_representation(self, instance):
#         print(instance)
#         return super().to_representation(instance)