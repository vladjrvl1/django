from django.db import models
from django.urls import reverse, reverse_lazy

'''
Categories: 
----------
title, slug, photo, content
'''

'''
Product:
---------
title, slug, category, brand, content, screen_size, screen_resolution, ram, photo, memory, price, views, created_at
'''


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, verbose_name='URL')
    content = models.TextField(blank=True, null=True, verbose_name='Content')
    photo = models.ImageField(upload_to='categories/%y/%m/%d', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']

class Brand(models.Model):
    title = models.CharField(max_length=255, verbose_name='Brand')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('smartphone', kwargs={"slug": self.slug})


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Category')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Brand')
    content = models.TextField(blank=True, null=True, verbose_name='Content')
    photo = models.ImageField(upload_to='products/%y/%m/%d/', verbose_name='Photo', blank=True, null=True)
    photo1 = models.ImageField(upload_to='products/%y/%m/%d/', verbose_name='Photo 1', blank=True, null=True)
    photo2 = models.ImageField(upload_to='products/%y/%m/%d/', verbose_name='Photo 2', blank=True, null=True)
    photo3 = models.ImageField(upload_to='products/%y/%m/%d/', verbose_name='Photo 3', blank=True, null=True)
    photo4 = models.ImageField(upload_to='products/%y/%m/%d/', verbose_name='Photo 4', blank=True, null=True)
    price = models.PositiveIntegerField(verbose_name='Price')
    views = models.IntegerField(default=0, verbose_name='Views')

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Device(Product):
    screen_size = models.CharField(max_length=50, verbose_name='Screen size')
    screen_resolution = models.CharField(max_length=50, verbose_name='Screen Resolution')
    ram = models.PositiveSmallIntegerField(verbose_name='RAM, Gb')
    memory = models.PositiveSmallIntegerField(verbose_name='Memory, Gb')
    gpu = models.CharField(max_length=255, verbose_name='GPU')
    cpu = models.CharField(max_length=255, verbose_name='CPU')

    def get_absolute_url(self):
        # return reverse('product', kwargs={'category_slug': self.category.slug, 'slug': self.slug})
        # return reverse('product', args=[self.id, ])
        # return reverse_lazy('product', kwargs={"slug": self.slug})
        return reverse('product', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'

class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    photo = models.ImageField(upload_to='sliders/%y/%m/%d', blank=True, null=True, verbose_name='Slider image')


class SubscriberEmail(models.Model):
    email = models.EmailField(verbose_name='email', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


