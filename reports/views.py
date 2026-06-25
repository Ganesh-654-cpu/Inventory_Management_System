from django.shortcuts import render
from products.models import Product
from suppliers.models import Supplier
from purchases.models import Purchase
from sales.models import Sale
import openpyxl
from reportlab.pdfgen import canvas
from django.http import HttpResponse



def dashboard(request):

    purchases = Purchase.objects.all()
    sales = Sale.objects.all()

    query = request.GET.get('q')

    if query:
        recent_products = Product.objects.filter(
            name__icontains=query
        )
    else:
        recent_products = Product.objects.all().order_by('-id')[:5]

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
        "products": Product.objects.count(),
        "suppliers": Supplier.objects.count(),
        "purchases_count": Purchase.objects.count(),
        "sales_count": Sale.objects.count(),
        "purchases": purchases,
        "sales": sales,
        "total_purchase": total_purchase,
        "total_sales": total_sales,
        "profit": profit,
        "recent_products": recent_products,
    }

    return render(
        request,
        "reports/dashboard.html",
        context
    )
    
    
def export_products_excel(request):

    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = "Products"

    worksheet.append([
        "ID",
        "Product Name",
        "Category",
        "Quantity"
    ])

    products = Product.objects.all()

    for product in products:
        worksheet.append([
            product.id,
            product.name,
            str(product.category),
            product.quantity,
        ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response['Content-Disposition'] = (
        'attachment; filename=products.xlsx'
    )

    workbook.save(response)

    return response


def export_products_pdf(request):

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        'attachment; filename="products.pdf"'
    )

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, 800, "Products Report")

    y = 760

    products = Product.objects.all()

    for product in products:

        p.setFont("Helvetica", 12)

        p.drawString(
            50,
            y,
            f"{product.id} | {product.name} | Stock : {product.quantity}"
        )

        y -= 25

        if y < 50:
            p.showPage()
            y = 800

    p.save()

    return response
           
    