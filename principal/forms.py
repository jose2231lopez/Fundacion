from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=140, 
        required=True, 
        label='Nombre',
        error_messages={'required': 'Este campo es obligatorio.'}
    )
    last_name = forms.CharField(
        max_length=140, 
        required=False, 
        label='Apellido'
    )
    email = forms.EmailField(
        required=True, 
        label='Correo electrónico',
        error_messages={'invalid': 'Introduce un correo electrónico válido.'}
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        error_messages = {
            'username': {
                'required': 'Este campo es obligatorio.',
            },
            'password1': {
                'required': 'Este campo es obligatorio.',
            },
            'password2': {
                'required': 'Este campo es obligatorio.',
                'password_mismatch': 'Las contraseñas no coinciden.',
            },
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya está registrado, prueba con otro.')
        return email
    
from django import forms
from .models import Actividades

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividades
        fields = ['actividad_id', 'nombre_actividad','descripcion', 'fecha_actividad', 'estado']
        widgets = {
            'fecha_actividad': forms.DateInput(attrs={'type': 'date'}),
        }
from django import forms
from.models import Beneficiarios

class BeneficiarioForm(forms.ModelForm):
    class Meta:
        model = Beneficiarios
        fields = ['beneficiario_id','nombre', 'apellido','genero','telefono','grupo_etnico','email','fecha_registro']
        widgets = {
            'fecha_registro':forms.DateInput(attrs={'type':'date'}),
        }

from.models import Regiones

class RegionForm(forms.ModelForm):
    class Meta:
        model = Regiones
        fields = ['region_id','departamento','municipio','vereda']
