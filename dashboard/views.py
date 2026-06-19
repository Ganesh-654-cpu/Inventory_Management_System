from django.shortcuts import render
from products.models import Product
from suppliers.models import Supplier
from purchases.models import Purchase
from sales.models import Sale


def dashboard(request):

    low_stock = Product.objects.filter(quantity__lte=10)

    recent_products = Product.objects.order_by('-id')[:5]

    recent_purchases = Purchase.objects.order_by('-id')[:5]
    
    recent_sales = Sale.objects.order_by('-id')[:5]

    total_purchase_amount = sum(
        p.purchase_price * p.quantity
        for p in Purchase.objects.all()
    )

    total_sales_amount = sum(
        s.sale_price * s.quantity
        for s in Sale.objects.all()
    )

    total_profit = total_sales_amount - total_purchase_amount

    context = {
        'total_products': Product.objects.count(),
        'total_suppliers': Supplier.objects.count(),
        'total_purchases': Purchase.objects.count(),
        'total_sales': Sale.objects.count(),

        'expense': total_purchase_amount,
        'revenue': total_sales_amount,
        'profit': total_profit,

        'low_stock': low_stock,
        'recent_products': recent_products,
        'recent_purchases': recent_purchases,
        'recent_sales': recent_sales,
    }

    return render(request, 'dashboard/index.html', context)