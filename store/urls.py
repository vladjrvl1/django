from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('<str:slug>', get_category, name='category'),
    path('laptops/<str:slug>', get_laptop, name='laptop'),
    path('contact/', contact, name='contact'),
    path('cart/', cart, name='cart'),
]