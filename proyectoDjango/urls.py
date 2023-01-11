"""proyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from appDjango.views import mostrar_familiares, BuscarFamiliar, ActualizarFamiliar, AltaFamiliar, BorrarFamiliar, mostrar_mascotas, AltaMascota, ActualizarMascota, BuscarMascota, BorrarMascota, mostrar_vehiculos, BuscarVehiculo, AltaVehiculo, ActualizarVehiculo, BorrarVehiculo
from appBlog.views import index, PostList, PostCrear, PostActualizar, PostBorrar, PostDetalle, UserSignUp, UserLogin, UserLogOut, AvatarActualizar, UserActualizar, aboutme
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('appBlog/', index, name="appBlog-index"),
    path('appBlog/listar/', PostList.as_view(), name="appBlog-listar"),
    path('appBlog/crear/', PostCrear.as_view(), name="appBlog-crear"),
    path('appBlog/<int:pk>/actualizar/', PostActualizar.as_view(), name="appBlog-actualizar"),
    path('appBlog/<int:pk>/borrar/', PostBorrar.as_view(), name="appBlog-borrar"),
    path('appBlog/<int:pk>/detalle/', PostDetalle.as_view(), name="appBlog-detalle"),
    path('appBlog/registro', UserSignUp.as_view(), name="appBlog-registro"),
    path('appBlog/ingresar', UserLogin.as_view(), name="appBlog-ingresar"),
    path('appBlog/salir', UserLogOut.as_view(), name="appBlog-salir"),
    path('appBlog/avatar/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="appBlog-avatar-actualizar"),
    path('appBlog/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="appBlog-user-actualizar"),
    path('appBlog/acerca-de-mi', aboutme, name="appBlog-acerca-de-mi")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)