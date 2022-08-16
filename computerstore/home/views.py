from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import PC, Accessory, Type, News
from .forms import *
from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


class HomePage(ListView):
    model = News
    template_name = 'home/homepage.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class ComputerPage(ListView):
    model = PC
    template_name = 'home/computerpage.html'
    context_object_name = 'pc'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Computer Shop'
        return context


class AccessoryPage(ListView):
    model = Accessory
    template_name = 'home/accessorypage.html'
    context_object_name = 'acc'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Accessory Shop'
        return context


class DetailComputerPage(DetailView):
    model = PC
    context_object_name = 'pcdetail'
    template_name = 'home/computerdetailpage.html'
    

class DetailAccessoryPage(DetailView):
    model = Accessory
    context_object_name = 'accdetail'
    template_name = 'home/accessorydetailpage.html'


class AddAnAdvertPageN(CreateView):
    form_class = NewsForm
    template_name = "home/addanadvertpage_news.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add An Advert'
        return context


class AddAnAdvertPageC(CreateView):
    form_class = PCForm
    template_name = "home/addanadvertpage_pc.html"
    success_url = "/computers/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add An Advert'
        return context


class AddAnAdvertPageA(CreateView):
    form_class = AccessoryForm
    template_name = "home/addanadvertpage_acc.html"
    success_url = "/accessories/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add An Advert'
        return context

class RegisterPage(CreateView):
    form_class = RegisterForm
    template_name = "home/register.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        return context

def user_logout(request):
    logout(request)
    return redirect('home')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно авторизовались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка авторизации')
    else:
        form = LoginForm() 
    return render(request, 'home/login.html', {"form": form})