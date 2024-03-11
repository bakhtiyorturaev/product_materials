import uuid
from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.product_name


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductMaterials(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    material_name = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)


class Warehouse(models.Model):
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)
    remainder = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
