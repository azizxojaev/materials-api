from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=150, db_index=True)
    product_qty = models.PositiveIntegerField()

    def __str__(self):
        return self.product_name


class Material(models.Model):
    material_name = models.CharField(max_length=150, db_index=True)
    
    def __str__(self):
        return f'{self.material_name} - {self.id}'


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product} - {self.material}'
    

class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, db_index=True, unique=True)
    remainder = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.material.material_name} - {self.id}'