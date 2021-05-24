from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail
from django.db.models import F
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import ContactForm, NewsLetterForm


class Home(ListView):
    model = Laptop
    template_name = 'store/index.html'
    context_object_name = 'laptops'
    paginate_by = 12
    form = ContactForm()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'HOME PAGE'
        context['sliders'] = Slider.objects.all()
        context['categories'] = Category.objects.all()
        context['cat_laptop'] = context['categories'].get(slug='laptops')
        context['cat_smartphone'] = context['categories'].get(slug='smartphones')
        return context


class CategoryView(ListView):
    model = Category
    paginate_by = 4
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


class Product(DetailView):
    paginate_by = 4
    context_object_name = 'product'
    template_name = 'store/product.html'

    def get_context_data(self, **kwargs):
        context = super(Product, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug='laptops') # сделать отзывчивость
        context['products'] = Laptop.objects.all().order_by('views')[:8] # КАК подставить сюда модель обьявляемую
        # в наследниках класса.objects.filter()
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class LaptopView(Product):
    model = Laptop


class SmartphoneView(Product):
    model = Smartphone


def cart(request):
    return render(request, 'store/cart.html')

def checkout(request):
    return render(request, 'store/checkout.html')




def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            message = 'Name: ' + form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name'] + '\n' + \
                      form.cleaned_data['message']
            mail = send_mail(form.cleaned_data['subject'], message, 'vladjrvl.work@gmail.com',
                             ['vladjrvl@gmail.com'], fail_silently=False)
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('contact')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка валидации')
    else:
        form = ContactForm()
    return render(request, 'store/contact.html', context={"form": form})


class NewsletterView(CreateView):
    model = NewsLetterRecipientEmail
    form_class = NewsLetterForm
    success_url = '/'


''' Поиск по товарам '''
# Сделать вывод всех товаров
class SearchView(ListView):
    paginate_by = 4
    context_object_name = 'products'
    template_name = 'store/search.html'

    def get_queryset(self):
        return Laptop.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context

