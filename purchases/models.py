
# Create your models here.

from django.db import models
from products.models import Product
from suppliers.models import Supplier


class Purchase(models.Model):
    invoice_no = models.CharField(max_length=50, unique=True)

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    purchase_date = models.DateField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # New purchase hone par stock increase hoga
        if not self.pk:
            self.product.quantity += self.quantity
            self.product.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice_no
