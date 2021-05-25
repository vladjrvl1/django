from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', CategoryView.as_view(), name='category'),
    path('category/<str:slug>', ProductView.as_view(), name='product'),
    # path(r'^category/(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/$', ProductView.as_view(), name='product'),  # лишние символы в Url
    path('search/', SearchView.as_view(), name='search'),
    path('contact/', contact, name='contact'),
    path('newsletter/', NewsletterView.as_view(), name='newsletter'),
    path('checkout/', checkout, name='checkout'),


]

# def product_view(request, slug, *args, **kwargs):
#     product = get_object_or_404(Product, slug=slug)
#     return render(request, 'store/product.html', {'product': product})
#
# class Product(models.Model):
#     def get_absolute_url(self):
#         return reverse('articles_subcategory', args=[str(self.category.slug), str(self.slug)])