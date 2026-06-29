
# Register your models here.

from django.contrib import admin
from .models import Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = (
        'invoice_no',
        'customer',
        'product',
        'quantity',
        'sale_price',
        'sale_date',
    )
