from django.urls import path
from . import views 


urlpatterns = [

    # path a dashboard de App Dash
    path('dash/',views.dashboardView, name = "dash"),

]

