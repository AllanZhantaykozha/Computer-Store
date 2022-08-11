from django.shortcuts import render
from django.views.generic import ListView
from .models import PC, Accessory, Type, News

#90887

class HomePage(ListView):
    model = News
    template_name = 'home/homepage.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context

class ComputerPage(ListView):
    model = PC
    template_name = 'home/computerpage.html'
    context_object_name = 'pc'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Computer Shop'
        return context

class AccessoryPage(ListView):
    model = Accessory
    template_name = 'home/accessorypage.html'
    context_object_name = 'acc'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Accessory Shop'
        return context