from django.shortcuts import render
from .models import Animals, Protectora, Colaborador
# Create your views here.
def lista_animales(request):
    animal = Animals.objects.all
    return render(request,'blog/Animals.html',{"varios_animales":animal})

def lista_protectora(request):
    protect = Protectora.objects.all
    return render(request,'blog/Protectoras.html',{"varias_protectoras":protect})

def lista_colaboradores(request):
    colab = Colaborador.objects.all
    return render(request,'blog/Colaboradores.html',{"varios_colaboradores":colab})