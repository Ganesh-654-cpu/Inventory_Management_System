
# # Register your models here.

# from django.contrib import admin
# from .models import Product


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'name',
#         'category',
#         'supplier',
#         'price',
#         'quantity',
#         'minimum_stock',
#     )

#     search_fields = (
#         'name',
#         'sku',
#     )

#     list_filter = (
#         'category',
#         'supplier',
#     )

#     list_per_page = 10
# from django.utils.html import format_html

# def product_image(self, obj):
#     if obj.image:
#         return format_html(
#             '<img src="{}" width="50" height="50"/>',
#             obj.image.url
#         )
#     return "No Image"

from django.contrib import admin
from django.utils.html import format_html
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'product_image',
        'name',
        'category',
        'supplier',
        'price',
        'quantity',
        'minimum_stock',
    )

    search_fields = (
        'name',
        'sku',
    )

    list_filter = (
        'category',
        'supplier',
    )

    list_per_page = 10

    def product_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:5px;">',
                obj.image.url
            )
        return "No Image"

    product_image.short_description = "Image"
