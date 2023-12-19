from django import forms
from .models import *
from django.core.exceptions import ValidationError
import re

def validar_formato_rut(rut):
    rut = re.compile(r'^\d{1,3}(?:\.\d{3}){2}\-\d|^\d{7,8}\-\d$')
    if not rut.match(rut):
        raise ValidationError('El formato del RUT es incorrecto')


class FormEstacionamiento(forms.ModelForm):
    class Meta:
        model = Estacionamiento
        fields = ['patente', 'modelo_auto','lugar', 'nombre_usuario_id', 'tipo_usuario', 'contacto']
        widgets = {
            'patente': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'modelo_auto': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'lugar': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'nombre_usuario_id': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'tipo_usuario': forms.widgets.Select(attrs={'class': 'form-control'}),
            'contacto': forms.widgets.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'patente': 'Patente',
            'modelo_auto': 'Modelo del Auto',
            'lugar': 'Lugar',
            'nombre_usuario_id': 'Nombre del Usuario',
            'tipo_usuario': 'Tipo de Usuario',
            'contacto': 'Contacto',
        }
        label_suffix = ''
    def clean(self):
        cleaned_data = super().clean()
        lugar = cleaned_data.get('lugar')


        if Estacionamiento.objects.filter(lugar=lugar).exists():
            self.add_error('lugar', 'Este lugar ya está ocupado')




class FormFiltroEstacionamiento(forms.Form):
    patente = forms.CharField(
        label='Buscar Patente',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la patente'})
    )

class FormAdministracion(forms.ModelForm):
    rut = forms.CharField(max_length=12)
    class Meta:
        model = Administracion
        fields = ['rut', 'habitacion', 'nombre_usuario_id', 'tipo_usuario', 'contacto']
        widgets = {
            'rut': forms.widgets.TextInput(attrs={'class': 'form-control'} ),
            'habitacion': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'nombre_usuario_id': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'tipo_usuario': forms.widgets.Select(attrs={'class': 'form-control'}),
            'contacto': forms.widgets.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'rut': 'Rut',
            'habitacion': 'Habitacion',
            'nombre_usuario_id': 'Nombre del Usuario',
            'tipo_usuario': 'Tipo de Usuario',
            'contacto': 'Contacto',
        }
        label_suffix = ''


    def clean_rut(self):
        rut = self.cleaned_data['rut']
        rut_regex = re.compile(r'^\d{6,8}-[\dkK]$')  
        if not rut_regex.match(rut):
            raise ValidationError('El formato del RUT es incorrecto')
        return rut





class FormFiltroAdministracion(forms.Form):
    rut= forms.CharField(
        label='Buscar Por Rut',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el rut'})
    )

class FormAdmin(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['username', 'password', 'tipo']
        widgets = {
            'username': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'password': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.widgets.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': 'Rut',
            'password': 'Password',
            'tipo': 'Tipo de usuario',
        }
        label_suffix = ''

    def clean_username(self):
        rut = self.cleaned_data['username']
        rut_regex = re.compile(r'^\d{6,8}-[\dkK]$')
        if not rut_regex.match(rut):
            raise ValidationError('El formato del RUT es incorrecto')
        return rut





class FormFiltroAdmin(forms.Form):
    username= forms.CharField(
        label='Buscar Persona',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese rut'})
    )


class FormFiltroSoli(forms.Form):
    rut= forms.CharField(
        label='Cargar solicitudes',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese rut'})
    )
