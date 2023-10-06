from django.urls import path
from . import views
urlpatterns = [
    path('',views.lista_animales,name='Animals'),
    path('Protectora/',views.lista_protectora,name='Protectora'),
    path('Colaboradores/',views.lista_colaboradores,name="Colaboradores"),
]
