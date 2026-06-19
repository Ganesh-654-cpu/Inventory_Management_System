from django.shortcuts import render
from purchases.models import Purchase
from sales.models import Sale

def report_dashboard(request):
    purchases = Purchase.objects.all()
    sales = Sale.objects.all()

    total_purchase = sum(
        p.purchase_price * p.quantity
        for p in purchases
    )

    total_sales = sum(
        s.sale_price * s.quantity
        for s in sales
    )

    profit = total_sales - total_purchase

    context = {
        "total_purchase": total_purchase,
        "total_sales": total_sales,
        "profit": profit,
        "purchases": purchases,
        "sales": sales,
    }

    return render(request, "reports/dashboard.html", context)