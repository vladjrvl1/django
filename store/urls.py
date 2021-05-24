from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', CategoryView.as_view(), name='category'),
    path('search/', SearchView.as_view(), name='search'),
    path('laptops/<str:slug>', LaptopView.as_view(), name='laptop'),
    path('smartphones/<str:slug>', SmartphoneView.as_view(), name='smartphone'),
    path('contact/', contact, name='contact'),
    path('cart/', cart, name='cart'),
    path('newsletter/', NewsletterView.as_view(), name='newsletter'),
    path('checkout/', checkout, name='checkout'),


]