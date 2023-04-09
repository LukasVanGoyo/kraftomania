from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Brewery


class HomeView(ListView):
    model = Brewery
    template_name = 'home.html'
    
