from django.contrib import admin

from .models import *


# Register your models here.
class CategAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


admin.site.register(categ, CategAdmin)


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


admin.site.register(products, ProductAdmin)
