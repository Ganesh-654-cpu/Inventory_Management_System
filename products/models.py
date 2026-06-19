from django.db import models
from categories.models import Category
from suppliers.models import Supplier


class Product(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=150)

    sku = models.CharField(
        max_length=50,
        unique=True
    )

    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    quantity = models.PositiveIntegerField(default=0)

    minimum_stock = models.PositiveIntegerField(default=5)

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name