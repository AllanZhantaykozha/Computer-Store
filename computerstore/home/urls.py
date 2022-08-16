from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('computers/', ComputerPage.as_view(), name='computer'),
    path('accessories/', AccessoryPage.as_view(), name='accessory'),
    path('computers/<str:slug>', DetailComputerPage.as_view(), name='detailpc'),
    path('accessories/<str:slug>', DetailAccessoryPage.as_view(), name='detailacc'),
    path('add_news/', AddAnAdvertPageN.as_view(), name='add_news'),
    path('add_pc/', AddAnAdvertPageC.as_view(), name='add_pc'),
    path('add_accessory/', AddAnAdvertPageA.as_view(), name='add_acc'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='login'),
]