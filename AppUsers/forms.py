from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import *
from AppUsers.models import *

class UserRegisterForm(UserCreationForm):
    
    first_name = forms.CharField(min_length=3, max_length=50, label="Nombre")
    last_name = forms.CharField(min_length=3, max_length=50, label="Apellido")
    email = forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    #fec_nac = forms.DateField(label="Fecha de nacimiento")
    #telefono = forms.IntegerField(label="Telefono")
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2" ]
        
        
        
class UserEditForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Correo electronico")
    password1= forms.CharField(label='Password', widget=forms.PasswordInput, required=False)
    password2= forms.CharField(label='Confirme Password', widget=forms.PasswordInput, required=False)
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        #la sig linea elimina ayuda en los campos
        help_texts = { k: "" for k in fields}


class AvatarForm(forms.Form):
    imagen = forms.ImageField()    
    
    
class PostForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'rows': 3}), required=True)            
    
    class Meta:
        model = Post
        fields = ['content']