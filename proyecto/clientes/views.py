from django.shortcuts import redirect, render

from .forms import PaisForm
from .models import Cliente, Pais


def index(request):
    return render(request, 'clientes/index.html')


def pais_list(request):
    paises = Pais.objects.all()
    contexto = {'paises': paises}
    return render(request, 'clientes/pais_list.html', contexto)


def cliente_list(request):
    clientes = Cliente.objects.all()
    contexto = {'clientes': clientes}
    return render(request, 'clientes/cliente_list.html', contexto)


def pais_create(request):
    if request.method == 'GET':
        form = PaisForm()

    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('clientes:pais_list')

    return render(request, 'clientes/pais_create.html', {'form': form})
