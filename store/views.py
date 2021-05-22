from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *

class Home(ListView):
    model = Laptop
    template_name = 'store/index.html'
    context_object_name = 'laptops'
    paginate_by = 12

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'HOME PAGE'
        context['brands'] = Brand.objects.all()
        context['smartphones'] = Smartphone.objects.all()
        return context


def get_category(request, slug):
    return render(request, 'store/category.html')

def contact(request):
    return render(request, 'store/contact.html')

def cart(request):
    return render(request, 'store/cart.html')

def get_laptop(request, slug):
    return render(request, 'store/cart.html')

