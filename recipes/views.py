from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Bem-vindo à página de Receitas!</h1>")