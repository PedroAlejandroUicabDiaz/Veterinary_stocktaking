#from django.db.models import fields
import django_filters
from .models import *

class StocktakingFilter(django_filters.FilterSet):
    class Meta:
        model = stocktaking_tb
        fields = ['SKU_id','CATE_id','LOC_id','description_product']