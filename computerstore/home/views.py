from django.shortcuts import render
from django.views.generic import ListView
from .models import PC, Accessory, Type, News


class HomePage(ListView):
    model = News
    template_name = 'home/homepage.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context