from django.urls import path

from . import views

app_name = 'productos'


urlpatterns = [
    path('', views.index, name='index'),
    path('productocategoria/list', views.productocategoria_list, name='productocategoria_list'),
]
