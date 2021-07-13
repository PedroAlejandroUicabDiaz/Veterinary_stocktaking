from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):

    class Meta:

        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
                'password1',
                'password2',
            ]

        labels = {
                'username':'Nombre de usuario',
                'first_name':'Nombre',
                'last_name':'Apellidos',
                'email':'Correo',
                'password1':'Contraseña',
                'password2': 'Nueva Contraseña',
        }
