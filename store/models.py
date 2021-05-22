from django.db import models
from django.urls import reverse

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
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, verbose_name='URL')
    content = models.TextField(blank=True, null=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='categories/%y/%m/%d', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

class Brand(models.Model):
    title = models.CharField(max_length=255, verbose_name='Бренд')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Бренд')
    content = models.TextField(blank=True, null=True, verbose_name='Описание')
    screen_size = models.CharField(max_length=50, verbose_name='Размер экрана')
    screen_resolution = models.CharField(max_length=50, verbose_name='Разрешение экрана')
    ram = models.PositiveSmallIntegerField(verbose_name='Оперативная память, Гб')
    memory = models.PositiveSmallIntegerField(verbose_name='Встроенная память, Гб')
    photo = models.ImageField(upload_to='products/%y/%m/%d/', verbose_name='Фото', blank=True, null=True)
    price = models.PositiveIntegerField(verbose_name='Цена')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Smartphone(Product):
    sim_amount = models.IntegerField(verbose_name='Количество SIM-карт')

    def get_absolute_url(self):
        return reverse('smartphone', kwargs={"slug": self.slug})


class Laptop(Product):
    gpu = models.CharField(max_length=255, verbose_name='Видеокарта')
    cpu = models.CharField(max_length=255, verbose_name='Процессор')

    def get_absolute_url(self):
        return reverse('laptop', kwargs={"slug": self.slug})
