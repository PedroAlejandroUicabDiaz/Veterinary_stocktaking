from django.db import models
from django.db.models.manager import ManagerDescriptor
from datetime import date
# Create your models here.

class category_catalog(models.Model): # cambio
    CATE_id = models.IntegerField(primary_key=True) # cambio
    category_name = models.CharField(max_length=25) # cambio

class measured_catalog(models.Model):
    MEA_id = models.IntegerField(primary_key=True)
    measured_catalog = models.CharField(max_length=20)

class location_catalog(models.Model):
    LOC_id = models.IntegerField(primary_key=True)
    location_product = models.CharField(max_length=20)

class stocktaking_tb(models.Model):
    SKU_id = models.CharField(max_length=20, primary_key=True, unique=True)
    CATE_id = models.ForeignKey(category_catalog, on_delete=models.CASCADE) # changes
    MEA_id = models.ForeignKey(measured_catalog, on_delete=models.CASCADE) # changes 
    LOC_id = models.ForeignKey(location_catalog, on_delete=models.CASCADE) #changes
    description_product = models.CharField(max_length=100, null=True, blank=True) # cambio
    brand_product = models.CharField(max_length=20, null=True, blank=True) # cambio
    final_price_list = models.FloatField()
    quantity_product = models.FloatField()
    expiration_date = models.DateField()
    agregation_date = models.DateField(default=date.today) # cambio
    lastupdated_date = models.DateField(auto_now=True) # cambio 
    cost_unit = models.FloatField()
