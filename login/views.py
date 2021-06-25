from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy 
from login.forms import RegistroForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# Vista principal de la App de Login
def indexView(request):
     return render(request,'index.html')
# url = http://localhost:8000/applogin/home/


# Vista del menu dashboard de la App Log in (reuiqeres estar logueado para acceder)
@login_required
def dashboardView(request):
    return render(request,'dashboard.html')
# url = http://localhost:8000/applogin/dashboard/

# Clase para la Vista Register (forms.py)
class RegistroUsuario(CreateView):
    model = User
    template_name= 'registration/register.html'
    form_class = RegistroForm
    success_url = reverse_lazy('login_url')

