from django.urls import path
from . import views

urlpatterns = [
    path("pais/list", views.pais_list)
]
