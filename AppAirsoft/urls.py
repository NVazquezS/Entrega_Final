from django.urls import path, include
from django.contrib import admin
from AppAirsoft.views import *
from AppUsers.views import *
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
import Airsoft.settings as settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", vista_inicio, name = "AppAirsoft-inicio"), 
    path("equipamiento/", vista_equipamiento, name = "AppAirsoft-equipamiento"),
    path("replica/", vista_replica, name="AppAirsoft-replica"),
    path("nosotros/", vista_nosotros, name="AppAirsoft-nosotros"),
    path("about/", vista_nosotros, name="AppAirsoft-nosotros"),
    
    path("accounts/login/", iniciar_sesion, name="AppUsers-iniciar-sesion"),
    path("accounts/signup/", registrar_usuario, name="AppUsers-register"),
    path("logout/", LogoutView.as_view(template_name="AppUsers/logout.html"), name="AppUsers-logout"),
    path("accounts/profile/", mostrar_perfil, name="AppUsers-mostrar-perfil"),
    path("perfil/editar/", editar_perfil, name="AppUsers-editar-perfil"),
    path("perfil/editar/avatar", agregar_avatar, name="AppUsers-editar-avatar"),
    path("messages/", mostrar_mensajes, name="AppUsers-mensajes"),
    
    path("promos/crear/", crear_promos, name="AppAirsoft-promos-create"),
    path("promos/editar/<id>", editar_promo, name = "AppAirsoft-promo-edit"),
    path("promos/", mostrar_promos, name="AppAirsoft-promos"),
    path("promos/borrar/<id>", eliminar_promo, name="AppAirsoft-promo-borrar"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )