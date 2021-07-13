from django.contrib import admin
from dashapp.models import stocktaking_tb, category_catalog, measured_catalog, location_catalog


# Register your models here.
#class stock_admin(admin.ModelAdmin):
 #   list_display=

admin.site.register(stocktaking_tb)
admin.site.register(category_catalog)
admin.site.register(measured_catalog)
admin.site.register(location_catalog)