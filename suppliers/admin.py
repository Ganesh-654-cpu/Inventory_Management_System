
# Register your models here.
from django.contrib import admin
from .models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'supplier_name',
        'email',
        'phone',
        'is_active',
    )

    search_fields = (
        'supplier_name',
        'email',
        'phone',
    )

    list_filter = ('is_active',)
    list_per_page = 10

