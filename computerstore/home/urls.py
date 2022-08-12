from django.urls import path
from .views import HomePage, ComputerPage, AccessoryPage, DetailComputerPage, DetailAccessoryPage


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('computers/', ComputerPage.as_view(), name='computer'),
    path('accessories/', AccessoryPage.as_view(), name='accessory'),
    path('computers/<str:slug>', DetailComputerPage.as_view(), name='detailpc'),
    path('accessories/<str:slug>', DetailAccessoryPage.as_view(), name='detailacc'),
]