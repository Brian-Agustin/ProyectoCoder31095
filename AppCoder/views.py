from django.shortcuts import render
from AppCoder.models import Curso
# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def curso(request):
    curso1 = Curso(nombre='python', camada=31095)
    curso1.save()
    contexto = {
        'curso': curso1
    }
    return render(request, 'AppCoder/curso.html', contexto)



