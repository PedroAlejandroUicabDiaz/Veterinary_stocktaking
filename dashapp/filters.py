#from django.db.models import fields
import django_filters
from .models import *

# Dashboard filter
class StocktakingFilter(django_filters.FilterSet):
    class Meta:
        # model where the filter will obtain the attributes
        model = stocktaking_tb
        # attributes that will appear on the filter card
        fields = ['SKU_id','CATE_id','LOC_id','description_product']
        # 
        # 
        # remove the comment of this option if you want get all attribute from the model
        """ 
        fields = '__all__'
        """