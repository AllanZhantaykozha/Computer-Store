from django.urls import path
from .views import HomePage, ComputerPage, AccessoryPage


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('computers/', ComputerPage.as_view(), name='computer'),
    path('accessories/', AccessoryPage.as_view(), name='accessory'),
#    path('contact/', ContactPage.as_view(), name='contact'),
]