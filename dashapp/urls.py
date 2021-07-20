from django.urls import path
from . import views 


urlpatterns = [

    # path del dashboard de appdash
    path('dash/',views.dashboardView, name = "dash"),

    # path del la pagina para descargar el .csv
    path('exportCSV/',views.export_csv, name = "exportCSV"),

    # path de products de appdash
    path('products/',views.productView, name = "products"),

    # path del form-create Products de appdash
    path('createProduct/',views.createProductView, name = "createProducts"),

    # path del form-update Products de appdash
    path('updateProduct/<str:pk>/',views.updateProductView, name = "updateProducts"),

    # path del form-remove Products de appdash
    path('removeProduct/<str:pk>/',views.removeProductView, name = "removeProducts"),

    # path del form-create Location de appdash
    path('createLocation/',views.createLocationView, name = "createLocation"),

    # path del form-update Location de appdash
    path('updateLocation/<str:pk>/',views.updateLocationView, name = "updateLocation"),

    # path del form-remove Locations de appdash
    path('removeLocations/<str:pk>/',views.removeLocationView, name = "removeLocations"),

    # path del form-create categories de appdash
    path('createCategory/',views.createCategoryView, name = "createCategory"),

    # path del form-update Categories de appdash
    path('updateCategory/<str:pk>/',views.updateCategoryView, name = "updateCategory"),

    # path del form-remove Categories de appdash
    path('removeCategory/<str:pk>/',views.removeCategoryView, name = "removeCategory"),

    # path del form-create Measureds de appdash
    path('createMeasured/',views.createMeasuredView, name = "createMeasured"),

    # path del form-update Measureds de appdash
    path('updateMeasured/<str:pk>/',views.updateMeasuredView, name = "updateMeasured"),

    # path del form-remove Medidas de appdash
    path('removeMeasured/<str:pk>/',views.removeMeasuredView, name = "removeMeasured"),

]

