from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}

class SmartphoneAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    save_as = True

class LaptopAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Smartphone, CategoryAdmin)
admin.site.register(Laptop, CategoryAdmin)

