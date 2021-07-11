from django.urls import path
from . import views 


urlpatterns = [

    # path del dashboard de appdash
    path('dash/',views.dashboardView, name = "dash"),

    # path de products de appdash
    path('products/',views.productView, name = "products"),

    # path del form products de appdash
    path('createProduct/',views.createProductView, name = "createProducts"),

    # path del form-update products de appdash
    path('updateProduct/<str:pk>/',views.updateProductView, name = "updateProducts"),

     # path del form-remove products de appdash
    path('removeProduct/<str:pk>/',views.removeProductView, name = "removeProducts"),

     # path del form-create Location de appdash
    path('createLocation/',views.createLocationView, name = "createLocation"),

    # path del form-update Location de appdash
    path('updateLocation/',views.updateLocationView, name = "updateLocation"),

]

