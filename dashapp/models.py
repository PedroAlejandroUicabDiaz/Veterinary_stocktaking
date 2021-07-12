from django.db import models
from django.db.models.manager import ManagerDescriptor
from datetime import date
# Create your models here.

class category_catalog(models.Model): 
    CATE_id = models.IntegerField(primary_key=True) 
    category_name = models.CharField(max_length=25)

    def __str__(self):
        return self.category_name

class measured_catalog(models.Model):
    MEA_id = models.IntegerField(primary_key=True)
    measured_catalog = models.CharField(max_length=20)

    def __str__(self):
        return self.measured_catalog

class location_catalog(models.Model):
    LOC_id = models.IntegerField(primary_key=True)
    location_product = models.CharField(max_length=20)

    def __str__(self):
        return self.location_product

class stocktaking_tb(models.Model):
    SKU_id = models.CharField(max_length=20, primary_key=True, unique=True)
    CATE_id = models.ForeignKey(category_catalog, on_delete=models.CASCADE) 
    MEA_id = models.ForeignKey(measured_catalog, on_delete=models.CASCADE)
    LOC_id = models.ForeignKey(location_catalog, on_delete=models.CASCADE)
    description_product = models.CharField(max_length=100, null=True, blank=True)
    brand_product = models.CharField(max_length=20, null=True, blank=True)
    final_price_list = models.FloatField()
    quantity_product = models.FloatField()
    expiration_date = models.DateField()
    agregation_date = models.DateField(default=date.today)
    lastupdated_date = models.DateField(auto_now=True)
    cost_unit = models.FloatField()

    def __str__(self):
        return self.brand_product

