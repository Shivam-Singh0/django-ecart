from pickle import EMPTY_DICT
from django.contrib import admin

from shop.models import Products, Order

# Register your models here.
admin.site.site_header = "E-Com site"
admin.site.site_title = "Shopping"
admin.site.index_title = "Manage ABC Title"
class ProductAdmin(admin.ModelAdmin):
    list_display =  ('title', 'price', 'category', 'image')
    search_fields = ('title',)
    list_editable = ('price',)
admin.site.register(Products, ProductAdmin)
admin.site.register(Order)