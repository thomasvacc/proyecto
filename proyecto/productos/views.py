from django.shortcuts import render

from .forms import ProductoCategoriaForm
from .models import ProductoCategoria


def index(request):
    return render(request, 'productos/index.html')


def productocategoria_list(request):
    productocategoria = ProductoCategoria.objects.all()
    contexto = {'productocategoria': productocategoria}
    return render(request, 'productos/productocategoria_list.html', contexto)


def productocategoria_create(request):
    if request.method == 'GET':
        form = ProductoCategoriaForm()

    if request.method == 'POST':
        form = ProductoCategoriaForm(request.POST)
        print(request.POST)

    return render(request, 'productos/productocategoria_create.html', {'form': form})
