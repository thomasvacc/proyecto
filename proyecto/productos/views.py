from django.shortcuts import render
from .models import ProductoCategoria


def index(request):
    return render(request, 'productos/index.html')


def productocategoria_list(request):
    productocategorias = ProductoCategoria.objects.all()
    contexto = {'productocategorias': productocategorias}
    return render(request, 'productos/productocategoria_list.html', contexto)
