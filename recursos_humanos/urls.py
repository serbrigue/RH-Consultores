from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('nosotros/',nosotros,name='nosotros'),
    path('empleados/',lista_empleados,name='empleados'),
    path('contacto/',contacto,name='contacto'),
    path("registro/",register,name='registro'),
    path('login/', login, name='login'),
     path('logout/', user_logout, name='logout'),
]
