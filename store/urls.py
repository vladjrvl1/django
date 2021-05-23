from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', CategoryView.as_view(), name='category'),
    path('laptops/<str:slug>', get_laptop, name='laptop'),
    path('smartphones/<str:slug>', get_smartphones, name='smartphone'),
    path('contact/', contact, name='contact'),
    path('cart/', cart, name='cart'),
]