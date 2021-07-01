from django.db import models
from django.db.models.manager import ManagerDescriptor

# Create your models here.
class stocktaking_tb(models.Model):
    SKU_id = models.CharField(max_length=20)
    CATE_id = models.IntegerField()
    description_product = models.CharField(max_length=100)
    brand_product = models.CharField(max_length=20)
    list_price = models.FloatField()
    quantity_product = models.FloatField()
    measured_unit = models.CharField(max_length=10)
    status_product = models.CharField(max_length=20)
    expiration_date = models.DateField()
    agregation_date = models.DateField()
    cost_unit = models.FloatField()

class catalog_categories(models.Model):
    CATE_id = models.IntegerField()
    category_name = models.CharField(max_length=20)
