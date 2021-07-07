from django.urls import path
from . import views 


urlpatterns = [

    # path del dashboard de appdash
    path('dash/',views.dashboardView, name = "dash"),

    # path de products de appdash
    path('products/',views.productView, name = "products"),

]

