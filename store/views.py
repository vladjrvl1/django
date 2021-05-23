from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
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
        context['sliders'] = Slider.objects.all()
        return context

class CategoryView(ListView):
    model = Category
    paginate_by = 12
    context_object_name = 'products'
    template_name = 'store/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        if self.kwargs['slug'] == 'smartphones':
            return qs.get(slug=self.kwargs['slug']).smartphone_set.all()
        elif self.kwargs['slug'] == 'laptops':
            return qs.get(slug=self.kwargs['slug']).laptop_set.all()
        else:
            return qs




def contact(request):
    return render(request, 'store/contact.html')

def cart(request):
    return render(request, 'store/cart.html')

def get_laptop(request, slug):
    return render(request, 'store/cart.html')

def get_smartphones(request, slug):
    return render(request, 'store/cart.html')
