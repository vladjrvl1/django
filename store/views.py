from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail
from django.db.models import F
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import ProcessFormView

from cart.forms import CartAddProductForm
from .models import *
from .forms import ContactForm, SubscriberEmailForm, MassMailForm


class Home(ListView):
    model = Device
    template_name = 'store/index.html'
    context_object_name = 'devices'
    paginate_by = 12
    form = ContactForm()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home Page'
        context['sliders'] = Slider.objects.all()
        context['cat_laptops'] = Category.objects.get(slug='laptops') # сделать тоже самое в шаблоне???
        context['cat_smartphones'] = Category.objects.get(slug='smartphones')
        context['cart_product_form'] = CartAddProductForm()

        return context


class CategoryView(ListView):
    model = Category
    paginate_by = 12
    context_object_name = 'products'
    template_name = 'store/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        context['cart_product_form'] = CartAddProductForm()
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.get(slug=self.kwargs['slug']).device_set.all()


class ProductView(DetailView):
    model = Device
    context_object_name = 'device'
    template_name = 'store/product.html'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['related_products'] = Device.objects.all().order_by('views')[:8]
        context['cart_product_form'] = CartAddProductForm()
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context

def checkout(request):
    return render(request, 'store/checkout.html')

def mass_mail(request):
    if request.method == "POST":
        form = MassMailForm(request.POST)
        if form.is_valid():
            recipients = [obj.email for obj in SubscriberEmail.objects.all()]
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['message'],
                             'vladjrvl.work@gmail.com', recipients)
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('massmail')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка валидации')
    else:
        form = MassMailForm()
    return render(request, 'store/mass_mail.html', {'form': form})


# class SendMassMail(ProcessFormView):
#     recipients = [obj.email for obj in SubscriberEmail.objects.all()]
#
#     def get(self, request, *args, **kwargs):
#         form = MassMailForm()
#         return form
#
#     def post(self, request, *args, **kwargs):
#         form = MassMailForm(request.POST)
#         if form.is_valid():
#             mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['message'], 'vladjrvl.work@gmail.com',
#                              self.recipients, fail_silently=False)
#             if mail:
#                 messages.success(request, 'Письмо отправлено')
#                 return redirect('contact')
#             else:
#                 return messages.error(request, 'Ошибка отправки')
#         else:
#             return messages.error(request, 'Ошибка валидации')



def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'From: ' + form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name'] + ' | ' + \
                      form.cleaned_data['subject']
            mail = send_mail(subject, form.cleaned_data['message'], 'vladjrvl.work@gmail.com',
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
    model = SubscriberEmail
    form_class = SubscriberEmailForm
    success_url = '/'



''' Поиск по товарам '''
# Сделать вывод всех товаров
class SearchView(ListView):
    paginate_by = 8
    context_object_name = 'products'
    template_name = 'store/search.html'

    def get_queryset(self):
        return Device.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context



def auth(request):
    return render(request, 'oauth.html')

