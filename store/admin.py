from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}

@admin.register(Device)
class Product(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    list_display = ['title', 'slug', 'photo', 'show_photo', 'price', 'views']
    list_editable = ['price', 'views']

    def show_photo(self, obj):
        if obj.photo:
            return mark_safe("<img src='{}' width=80/".format(obj.photo.url) )
        else:
            return "None"

    show_photo.__name__ = "Photo"

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    pass

@admin.register(NewsletterRecipientEmail)
class NewsLetterRecipientEmailAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at", )



