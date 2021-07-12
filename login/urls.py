from django.urls import path
from . import views 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from login.views import RegistroUsuario

urlpatterns = [

    # path a pagina de inicio
    path('home/',views.indexView,name="home"),

    # path a dashboard de App Log in
    path('dashboard/',views.dashboardView, name = "dashboard"),

    # path a login template 
    path('login/',LoginView.as_view(), name= "login_url"),

    # path a register template
    path('register/',RegistroUsuario.as_view(), name = "register_url"),

    # path a log out template
    path('logout/',LogoutView.as_view(next_page="home"), name = "logout"), 

    # path a password_change template
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'),
    name = 'password_change'),

    # path a password_change_done template
    path('password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
    name= 'password_change_done'),

    # path a password_reset template
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',
    html_email_template_name='registration/password_reset_email.html'), name='password_reset'),

    # path a password_reset_done template
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
    name='password_reset_done'),

    # path a password_reset_confirm
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
    name='password_reset_confirm'),

    # path a password_reset_complete
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    name='password_reset_complete'),

]