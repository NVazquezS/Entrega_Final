from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()
    nombre_usuario = forms.CharField()
    contrasenia = forms.CharField()

class EquipamientoForm(forms.Form):
    tipo_de_equipamiento = forms.CharField()
    precio = forms.IntegerField()
    accesorios = forms.CharField()

class ReplicaForm(forms.Form):
    nombre_replica = forms.CharField()
    precio = forms.IntegerField()
    imagen = forms.ImageField()

class PromoForm(forms.Form):
    nombre_promo = forms.CharField()
    precio = forms.IntegerField()
    imagen = forms.ImageField()