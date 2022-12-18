from django.shortcuts import render, redirect, get_object_or_404

#Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from AppUsers.forms import *
from AppUsers.models import *
from django.contrib.auth.models import User




# Create your views here.

def iniciar_sesion(request):
    
    errors = []
    
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])
            
            if user is not None:
                login(request, user)
                return redirect("AppUsers-mostrar-perfil")
            else:
                return render(request, "AppUsers/login.html", {"form": formulario, "errors": "Credenciales invalidas"} )
        else:
            return render(request, "AppUsers/login.html", {"form": formulario, "errors": formulario.errors} )    
    formulario = AuthenticationForm()
    return render (request, "AppUsers/login.html", {"form": formulario, "errors": errors} )
    
    
def registrar_usuario(request):
    
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        
        if formulario.is_valid():

            formulario.save()
            return redirect ("AppUsers-iniciar-sesion")
        else:
            return render (request, "AppUsers/register.html", {"form": formulario, "errors": formulario.errors})
    
    
    formulario = UserRegisterForm()

    return render (request, "AppUsers/register.html", {"form": formulario})



#@login_required
def mostrar_perfil(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        imagen_model = Avatar.objects.get(user=request.user.id).order_by("-id")[0]
        imagen_url = imagen_model.imagen.url
                
    else:
        
        user = current_user
        imagen_url = ""
    return render (request, "AppUsers/perfil.html", {"user": user, "imagen_url": imagen_url})


@login_required
def editar_perfil(request):
    usuario = request.user
    
    if request.method =="POST":
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.email = data["email"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
        
            usuario.save()
            return redirect("AppUsers-mostrar-perfil")
        
        else:
            return render(request, "AppUsers/editar_perfil.html", {"form": formulario, "errors": formulario.errors})
    else:
        formulario = UserEditForm(initial= {"email": usuario.email, "first_name": usuario.first_name, "last_name": usuario.last_name })
    
    return render(request, "AppUsers/editar_perfil.html",{"form": formulario})

@login_required
def mostrar_mensajes(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method =="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            
            return redirect('AppUsers-mensajes')
    else:
        form= PostForm()   
    posts = Post.objects.all()
    return render(request, "AppUsers/mensajes.html", {"posts": posts, "form": form})

@login_required
def agregar_avatar(request):
    
    if request.method == "POST":
        formulario = AvatarForm(request.POST, request.FILES)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = request.user
            avatar = Avatar(user=usuario, imagen=data["imagen"])
            avatar.save()
            
            return redirect("AppUsers-mostrar-perfil")
        else:
            return render(request, "AppUsers/agregar_avatar.html" , {"form": formulario, "errors": formulario.errors})
    formulario = AvatarForm()
    return render(request, "AppUsers/agregar_avatar.html", {"form": formulario})


