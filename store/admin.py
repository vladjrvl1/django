from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}

@admin.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    save_as = True

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    pass

@admin.register(NewsLetterRecipientEmail)
class NewsLetterRecipientEmailAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at", )



