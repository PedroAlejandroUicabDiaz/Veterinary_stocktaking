from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from .models import stocktaking_tb,measured_catalog,category_catalog,location_catalog

# Get the form to visualize it on the respective html -- ADD NEW PRODUCT
class ProductForm(ModelForm):
    class Meta:
        model = stocktaking_tb
        fields = '__all__'

# Get the form to visualize it on the respective html -- ADD NEW CATEGORY
class CategoryForm(ModelForm):
    class Meta:
        model = category_catalog
        fields = '__all__'

# Get the form to visualize it on the respective html -- ADD NEW MEASURE
class MeasuredForm(ModelForm):
    class Meta:
        model = measured_catalog
        fields = '__all__'

# Get the form to visualize it on the respective html -- ADD NEW LOCATION
class LocationForm(ModelForm):
    class Meta:
        model = location_catalog
        fields = '__all__'