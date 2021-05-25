from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}

@admin.register(Device)
class LaptopAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    pass

@admin.register(NewsletterRecipientEmail)
class NewsLetterRecipientEmailAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at", )



