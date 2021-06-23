from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# Vista principal de la App de Login
def indexView(request):
     return render(request,'index.html')
    # url = http://localhost:8000/applogin/home/


# Vista del menu dashboard de la App Login (reuiqeres estar logueado para acceder)
@login_required
def dashboardView(request):
    return render(request,'dashboard.html')
# url = http://localhost:8000/applogin/dashboard/


# Vista para registro del usuario nuevo
def registerView(request):

    # Si ya se mando algo
    if request.method == "POST":

        # Crea un formulario con lo que se mando
        form = UserCreationForm(request.POST)

        # Si el formulario es valido
        if form.is_valid():

            # Guardalo y redirecciona 
            form.save()
            return redirect('login_url')

        else:
            return HttpResponse('Datos no aceptados! \nIncumplimiento de lineamientos o el usuario ya esta registrado!')
    
    # Al principio no se ha mandado nada
    else:
        # Crea el formulario vacio
        form = UserCreationForm()

    return render(request,'registration/register.html',{'form':form})
    # url = http://localhost:8000/applogin/register/


    # url de pagina de login = http://localhost:8000/applogin/login/ 