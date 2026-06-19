
# Register your models here.

from django.contrib import admin
from .models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = (
        'invoice_no',
        'product',
        'supplier',
        'quantity',
        'purchase_price',
        'purchase_date',
    )

    search_fields = (
        'invoice_no',
    )

    list_filter = (
        'purchase_date',
        'supplier',
    )

    list_per_page = 10
