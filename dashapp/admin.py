from django.contrib import admin
from dashapp.models import stocktaking_tb, catalog_categories


# Register your models here.
#class stock_admin(admin.ModelAdmin):
 #   list_display=

admin.site.register(stocktaking_tb)
admin.site.register(catalog_categories)