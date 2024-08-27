from django import forms

from .models import ProductoCategoria


class ProductoCategoriaForm(forms.ModelForm):
    class Meta:
        model = ProductoCategoria
        fields = ['nombre', 'descripcion']
