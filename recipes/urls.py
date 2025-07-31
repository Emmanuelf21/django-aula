from django.urls import path #importar a função path do modulo de urls do django
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipes_list'),
]