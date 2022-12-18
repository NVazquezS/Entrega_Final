from django.shortcuts import render, redirect
from AppAirsoft.models import * 
from AppAirsoft.forms import *
from AppUsers.models import * 
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test


# Creamos nuestras views

def vista_inicio(request):
    if request.user.is_authenticated:
        imagen_model = Avatar.objects.filter(user=request.user.id).order_by("-id")[0]
        imagen_url = imagen_model.imagen.url
    else:
        imagen_url = ""    
    return render(request, "Airsoft\index.html", {"imagen_url": imagen_url} )


def vista_equipamiento(request):
    if request.method == "POST":
        formulario = EquipamientoForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            equipamiento = Equipamiento(tipo_de_equipamiento = data["tipo_de_equipamiento"], precio = data["precio"], accesorios = data["accesorios"])
            equipamiento.save()
    formulario = EquipamientoForm()
    return render(request, "Airsoft/equipamiento.html", {"formulario": formulario})

def vista_replica(request):
    if request.method == "POST":
        formulario = ReplicaForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            replica = Replica(nombre_replica = data["nombre_replica"], precio = data["precio"])
            replica.save()
    formulario = ReplicaForm()
    return render(request, "Airsoft/replica.html", {"formulario": formulario})



def vista_nosotros(request):
    return render(request, "Airsoft/about.html")




@user_passes_test(lambda u: u.is_superuser)
def crear_promos(request):
    
    errores = ""
    if request.method == "POST":    #Validamos tipo de peticion
        
        formulario = PromoForm(request.POST, request.FILES)      #Cargamos los datos en el formulario
        
        if formulario.is_valid():       #Validamos los datos
            data = formulario.cleaned_data  #Recuperamos los datos sanitizados
            promo = Promos(nombre_promo=data["nombre_promo"], precio=data["precio"], imagen=data["imagen"]) #Creamos el curso
            promo.save()    #Guardamos el curso
            return redirect("AppAirsoft-promos")
        else:
            errores = formulario.errors()    #Si el formulario no es valido, mostramos errores
            
    formulario = PromoForm()      #Creamos formulario vacio
    contexto = {"formulario": formulario ,"errores": errores} #Creamos contexto
    
    return render(request, "Airsoft/crear_promo.html", contexto )       #Retornamos la respuesta




def mostrar_promos(request):
    promos = Promos.objects.all()
    return render(request, "Airsoft/promos.html", {"promos": promos})


@user_passes_test(lambda u: u.is_superuser)
def editar_promo(request, id):
    
    equipo = Promos.objects.get(id=id)
    if request.method == "POST":
        formulario = PromoForm(request.POST, request.FILES )

        if formulario.is_valid():
            data = formulario.cleaned_data

            equipo.nombre_promo = data["nombre_promo"]
            equipo.precio = data["precio"]
            equipo.imagen = data["imagen"]
            equipo.save()
            return redirect("AppAirsoft-promos")
        else:
            return render(request, "Airsoft/editar_promo.html", {"formulario": formulario, "errores": ""})
    else:
        formulario = PromoForm(initial = { "nombre_promo": Promos.nombre_promo, "precio": Promos.precio, "imagen": Promos.imagen})
    return render(request, "Airsoft/editar_promo.html", {"formulario": formulario})


@user_passes_test(lambda u: u.is_superuser)
def eliminar_promo(request, id):
    promo = Promos.objects.get(id=id)
    promo.delete()
    
    return redirect("AppAirsoft-promos")