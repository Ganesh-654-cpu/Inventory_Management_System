
# Create your models here.

from django.db import models
from products.models import Product


class Sale(models.Model):
    invoice_no = models.CharField(max_length=50, unique=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()

    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

    sale_date = models.DateField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if not self.pk:
            if self.product.quantity < self.quantity:
                raise ValueError("Not enough stock available")

            self.product.quantity -= self.quantity
            self.product.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice_no
