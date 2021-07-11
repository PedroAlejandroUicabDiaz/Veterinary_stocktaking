from django.db.models import fields
from django.forms import ModelForm
from .models import stocktaking_tb

class ProductForm(ModelForm):
    class Meta:
        model = stocktaking_tb
        fields = '__all__'
        
