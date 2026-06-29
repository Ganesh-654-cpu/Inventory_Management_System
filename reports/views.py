# from django.shortcuts import render
# from django.http import HttpResponse
# from django.db.models import Sum
# from products.models import Product
# from suppliers.models import Supplier
# from purchases.models import Purchase
# from sales.models import Sale
# from reportlab.pdfgen import canvas
# from django.db.models.functions import TruncMonth
# from customers.models import Customer
# from django.contrib.auth.decorators import login_required
# import openpyxl
# import json


# @login_required
# def dashboard(request):
    
#     if not (
#         request.user.groups.filter(name="Admin").exists() or
#         request.user.groups.filter(name="Manager").exists()
#     ):
#         return HttpResponse("Access Denied")


#     purchases = Purchase.objects.all()
#     sales = Sale.objects.all()
    
#     from_date = request.GET.get("from_date")
#     to_date = request.GET.get("to_date")
    
#     if from_date and to_date:
#         purchases = purchases.filter(
#         created_at__date__range=[from_date, to_date]
#     )
#     sales = sales.filter(
#         sale_date__range=[from_date, to_date]
#     )
    
#     sales_labels = []
#     sales_data = []

#     for sale in sales:
#         sales_labels.append(sale.product.name)
#         sales_data.append(sale.quantity)
    
    
#     sales = Sale.objects.all()
    
#     from_date = request.GET.get("from_date")
#     to_date = request.GET.get("to_date")

#     if from_date and to_date:
#         purchases = purchases.filter(
#         created_at__date__range=[from_date, to_date]
#     )

#     sales = sales.filter(
#         sale_date__range=[from_date, to_date]
#     )

#     sales_labels = []
#     sales_data = []

#     for sale in sales:
#         sales_labels.append(sale.product.name)
#         sales_data.append(sale.quantity)

#     query = request.GET.get("q")

#     if query:
#         recent_products = Product.objects.filter(name__icontains=query)
#     else:
#         recent_products = Product.objects.all().order_by("-id")[:5]

#     total_purchase = sum(
#         p.purchase_price * p.quantity
#         for p in purchases
#     )

#     total_sales = sum(
#         s.sale_price * s.quantity
#         for s in sales
#     )

#     profit = total_sales - total_purchase
    
#     last_month_sales = (
#     Sale.objects
#     .annotate(month=TruncMonth("sale_date"))
#     .values("month")
#     .annotate(total=Sum("sale_price"))
#     .order_by("-month")[:2]
# )

#     growth = 0

#     if len(last_month_sales) >= 2:
#         current = float(last_month_sales[0]["total"] or 0)
#         previous = float(last_month_sales[1]["total"] or 0)

#         if previous > 0:
#             growth = round(((current - previous) / previous) * 100, 2)

#     else:
#         current = 0
#         previous = 0

#     low_stock_products = Product.objects.filter(quantity__lte=5)

#     category_data = {}

#     for product in Product.objects.all():
#         category = str(product.category)

#         if category in category_data:
#             category_data[category] += product.quantity
#         else:
#             category_data[category] = product.quantity

#     category_labels = list(category_data.keys())
#     category_stock = list(category_data.values())
#     recent_sales = Sale.objects.order_by("-id")[:5]
#     recent_purchases = Purchase.objects.order_by("-id")[:5]
#     top_products = (
#     Sale.objects.values("product__name")
#     .annotate(total_sold=Sum("quantity"))
#     .order_by("-total_sold")[:5]
#  )
    
#     monthly_sales = (
#     Sale.objects
#     .annotate(month=TruncMonth("sale_date"))
#     .values("month")
#     .annotate(total=Sum("quantity"))
#     .order_by("month")
# )
    

#     context = {
#         "products": Product.objects.count(),
#         "suppliers": Supplier.objects.count(),
#         "purchases_count": Purchase.objects.count(),
#         "sales_count": Sale.objects.count(),
#         "customers":Customer.objects.count(),
        

#         "purchases": purchases,
#         "sales": sales,

#         "total_purchase": total_purchase,
#         "total_sales": total_sales,
#         "profit": profit,

#         "recent_products": recent_products,
#         "recent_sales": recent_sales,
#         "recent_purchases": recent_purchases,

#         "sales_labels": json.dumps(sales_labels),
#         "sales_data": json.dumps(sales_data),

#         "low_stock_products": low_stock_products,
#         "top_products": top_products,

#         "category_labels": json.dumps(category_labels),
#         "category_stock": json.dumps(category_stock),
#         "monthly_sales": monthly_sales,
#         "growth": growth,
#         "customers":customers,
        
        
#         "monthly_labels": json.dumps([
#     sale["month"].strftime("%b %Y")
#     for sale in monthly_sales
# ]),

# "monthly_data": json.dumps([
#     sale["total"]
#     for sale in monthly_sales
# ]),

#     } 
#     return render(
#         request,
#         "reports/dashboard.html",
#         context,
#     )


# def export_products_excel(request):

#     workbook = openpyxl.Workbook()
#     worksheet = workbook.active
#     worksheet.title = "Products"

#     worksheet.append([
#         "ID",
#         "Product Name",
#         "Category",
#         "Quantity",
#     ])

#     for product in Product.objects.all():
#         worksheet.append([
#             product.id,
#             product.name,
#             str(product.category),
#             product.quantity,
#         ])

#     response = HttpResponse(
#         content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#     )

#     response["Content-Disposition"] = (
#         "attachment; filename=products.xlsx"
#     )

#     workbook.save(response)

#     return response


# def export_products_pdf(request):

#     response = HttpResponse(content_type="application/pdf")
#     response["Content-Disposition"] = 'attachment; filename="products.pdf"'

#     pdf = canvas.Canvas(response)

#     pdf.setFont("Helvetica-Bold", 16)
#     pdf.drawString(200, 800, "Products Report")

#     y = 760

#     for product in Product.objects.all():

#         pdf.setFont("Helvetica", 12)
#         pdf.drawString(
#             50,
#             y,
#             f"{product.id} | {product.name} | Stock: {product.quantity}",
#         )

#         y -= 25

#         if y < 50:
#             pdf.showPage()
#             y = 800

#     pdf.save()

#     return response






from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from products.models import Product
from suppliers.models import Supplier
from purchases.models import Purchase
from sales.models import Sale
from reportlab.pdfgen import canvas
from django.db.models.functions import TruncMonth
from customers.models import Customer
from django.contrib.auth.decorators import login_required
import openpyxl
import json


@login_required
def dashboard(request):

    if not (
        request.user.groups.filter(name="Admin").exists() or
        request.user.groups.filter(name="Manager").exists()
    ):
        return HttpResponse("Access Denied")

    purchases = Purchase.objects.all()
    sales = Sale.objects.all()

    from_date = request.GET.get("from_date")
    to_date = request.GET.get("to_date")

    if from_date and to_date:
        purchases = purchases.filter(created_at__date__range=[from_date, to_date])
        sales = sales.filter(sale_date__range=[from_date, to_date])

    sales_labels = []
    sales_data = []

    for sale in sales:
        sales_labels.append(sale.product.name)
        sales_data.append(sale.quantity)

    query = request.GET.get("q")

    if query:
        recent_products = Product.objects.filter(name__icontains=query)
    else:
        recent_products = Product.objects.all().order_by("-id")[:5]

    total_purchase = sum(p.purchase_price * p.quantity for p in purchases)
    total_sales = sum(s.sale_price * s.quantity for s in sales)
    profit = total_sales - total_purchase

    last_month_sales = (
        Sale.objects
        .annotate(month=TruncMonth("sale_date"))
        .values("month")
        .annotate(total=Sum("sale_price"))
        .order_by("-month")[:2]
    )

    growth = 0
    if len(last_month_sales) >= 2:
        current = float(last_month_sales[0]["total"] or 0)
        previous = float(last_month_sales[1]["total"] or 0)
        if previous > 0:
            growth = round(((current - previous) / previous) * 100, 2)

    low_stock_products = Product.objects.filter(quantity__lte=5)

    category_data = {}
    for product in Product.objects.all():
        category = str(product.category)
        if category in category_data:
            category_data[category] += product.quantity
        else:
            category_data[category] = product.quantity

    category_labels = list(category_data.keys())
    category_stock = list(category_data.values())

    recent_sales = Sale.objects.order_by("-id")[:5]
    recent_purchases = Purchase.objects.order_by("-id")[:5]
    recent_customers = Customer.objects.order_by("-id")[:5]

    top_products = (
        Sale.objects.values("product__name")
        .annotate(total_sold=Sum("quantity"))
        .order_by("-total_sold")[:5]
    )

    monthly_sales = (
        Sale.objects
        .annotate(month=TruncMonth("sale_date"))
        .values("month")
        .annotate(total=Sum("quantity"))
        .order_by("month")
    )

    context = {
        "products": Product.objects.count(),
        "suppliers": Supplier.objects.count(),
        "purchases_count": Purchase.objects.count(),
        "sales_count": Sale.objects.count(),
        "customers": Customer.objects.count(),

        "purchases": purchases,
        "sales": sales,

        "total_purchase": total_purchase,
        "total_sales": total_sales,
        "profit": profit,

        "recent_products": recent_products,
        "recent_sales": recent_sales,
        "recent_purchases": recent_purchases,
        "recent_customers": recent_customers,

        "sales_labels": json.dumps(sales_labels),
        "sales_data": json.dumps(sales_data),

        "low_stock_products": low_stock_products,
        "top_products": top_products,

        "category_labels": json.dumps(category_labels),
        "category_stock": json.dumps(category_stock),
        "monthly_sales": monthly_sales,
        "growth": growth,

        "monthly_labels": json.dumps([
            sale["month"].strftime("%b %Y") for sale in monthly_sales
        ]),
        "monthly_data": json.dumps([
            sale["total"] for sale in monthly_sales
        ]),
    }

    return render(request, "reports/dashboard.html", context)


def export_products_excel(request):

    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = "Products"

    worksheet.append(["ID", "Product Name", "Category", "Quantity"])

    for product in Product.objects.all():
        worksheet.append([
            product.id,
            product.name,
            str(product.category),
            product.quantity,
        ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=products.xlsx"
    workbook.save(response)
    return response


def export_products_pdf(request):

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="products.pdf"'

    pdf = canvas.Canvas(response)
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, 800, "Products Report")

    y = 760
    for product in Product.objects.all():
        pdf.setFont("Helvetica", 12)
        pdf.drawString(50, y, f"{product.id} | {product.name} | Stock: {product.quantity}")
        y -= 25
        if y < 50:
            pdf.showPage()
            y = 800

    pdf.save()
    return response