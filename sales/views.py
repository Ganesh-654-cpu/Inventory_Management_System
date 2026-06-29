# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Sale
# from reportlab.pdfgen import canvas
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# import qrcode
# from io import BytesIO
# import base64
# from django.core.mail import EmailMessage
# from django.conf import settings
# from decimal import Decimal
# import barcode
# from barcode.writer import ImageWriter
# import os
# from django.conf import settings


# @login_required
# def sale_list(request):

#     if not (
#         request.user.groups.filter(name="Admin").exists() or
#         request.user.groups.filter(name="Staff").exists()
#     ):
#         return HttpResponse("Access Denied")

#     sales = Sale.objects.all()

#     return render(request, "sales/sale_list.html", {"sales": sales})


# @login_required
# def invoice(request, id):

#     if not (
#         request.user.groups.filter(name="Admin").exists() or
#         request.user.groups.filter(name="Staff").exists()
#     ):
#         return HttpResponse("Access Denied")

#     sale = get_object_or_404(Sale, id=id)

#     total = sale.quantity * sale.sale_price
#     gst = total * Decimal("0.18")
#     cgst = total * Decimal("0.09")
#     sgst = total * Decimal("0.09")
#     grand_total = total + gst

#     customer_name = sale.customer.name if sale.customer else "Walk-in Customer"

#     invoice_data = f"""
# Invoice No : {sale.invoice_no}
# Customer : {customer_name}
# Product : {sale.product.name}
# Total : ₹{grand_total}
# """

#     qr = qrcode.make(invoice_data)
#     buffer = BytesIO()
#     qr.save(buffer, format="PNG")
#     qr_code = base64.b64encode(buffer.getvalue()).decode()

#     context = {
#         "sale": sale,
#         "total": total,
#         "gst": gst,
#         "cgst": cgst,
#         "sgst": sgst,
#         "grand_total": grand_total,
#         "qr_code": qr_code,
#         "customer_name": customer_name,
#         "barcode": barcode_url,
#     }

#     return render(request, "sales/invoice.html", context)


# def download_invoice(request, id):

#     sale = get_object_or_404(Sale, id=id)

#     response = HttpResponse(content_type="application/pdf")
#     response["Content-Disposition"] = (
#         f'attachment; filename="Invoice_{sale.invoice_no}.pdf"'
#     )

#     pdf = canvas.Canvas(response)

#     total = sale.quantity * sale.sale_price
#     gst = total * Decimal("0.18")
#     grand_total = total + gst

#     customer_name = sale.customer.name if sale.customer else "Walk-in Customer"

#     pdf.setFont("Helvetica-Bold", 18)
#     pdf.drawString(180, 800, "SALES INVOICE")

#     pdf.setFont("Helvetica", 12)
#     pdf.drawString(50, 750, f"Invoice No : {sale.invoice_no}")
#     pdf.drawString(50, 730, f"Customer : {customer_name}")
#     pdf.drawString(50, 710, f"Product : {sale.product.name}")
#     pdf.drawString(50, 690, f"Quantity : {sale.quantity}")
#     pdf.drawString(50, 670, f"Price : ₹{sale.sale_price}")
#     pdf.drawString(50, 650, f"Total : ₹{total}")
#     pdf.drawString(50, 630, f"GST (18%) : ₹{gst}")
#     pdf.drawString(50, 610, f"Grand Total : ₹{grand_total}")

#     pdf.save()

#     return response


# @login_required
# def send_invoice_email(request, id):

#     sale = get_object_or_404(Sale, id=id)

#     if not sale.customer or not sale.customer.email:
#         return HttpResponse("Customer email not found.")

#     customer_name = sale.customer.name if sale.customer else "Walk-in Customer"

#     subject = f"Invoice {sale.invoice_no}"

#     message = f"""
# Hello {customer_name},

# Thank you for your purchase.

# Invoice No : {sale.invoice_no}
# Product : {sale.product.name}
# Quantity : {sale.quantity}
# Total : ₹{sale.quantity * sale.sale_price}

# Thank You.
# """

#     email = EmailMessage(
#         subject,
#         message,
#         settings.EMAIL_HOST_USER,
#         [sale.customer.email],
#     )
#     email.send()

#     return HttpResponse("Invoice Email Sent Successfully.")

# barcode_class = barcode.get_barcode_class('code128')

# barcode_obj = barcode_class(
#     sale.invoice_no,
#     writer=ImageWriter()
# )

# barcode_path = os.path.join(
#     settings.MEDIA_ROOT,
#     f"{sale.invoice_no}_barcode"
# )

# barcode_obj.save(barcode_path)

# barcode_url = (
#     settings.MEDIA_URL +
#     f"{sale.invoice_no}_barcode.png"
# )




from django.shortcuts import render, get_object_or_404, redirect
from .models import Sale
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import qrcode
from io import BytesIO
import base64
from django.core.mail import EmailMessage
from django.conf import settings
from decimal import Decimal
import barcode
from barcode.writer import ImageWriter
import os


def is_authorized(user):
    return (
        user.groups.filter(name="Admin").exists() or
        user.groups.filter(name="Staff").exists()
    )


def generate_barcode(invoice_no):
    barcode_class = barcode.get_barcode_class("code128")
    barcode_obj = barcode_class(invoice_no, writer=ImageWriter())
    barcode_path = os.path.join(settings.MEDIA_ROOT, f"{invoice_no}_barcode")
    barcode_obj.save(barcode_path)
    barcode_url = settings.MEDIA_URL + f"{invoice_no}_barcode.png"
    return barcode_url


def generate_qr(invoice_no, customer_name, product_name, grand_total):
    invoice_data = f"""
Invoice No : {invoice_no}
Customer   : {customer_name}
Product    : {product_name}
Total      : ₹{grand_total}
"""
    qr = qrcode.make(invoice_data)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    qr_code = base64.b64encode(buffer.getvalue()).decode()
    return qr_code


@login_required
def sale_list(request):
    if not is_authorized(request.user):
        return HttpResponse("Access Denied")

    sales = Sale.objects.all()
    return render(request, "sales/sale_list.html", {"sales": sales})


@login_required
def invoice(request, id):
    if not is_authorized(request.user):
        return HttpResponse("Access Denied")

    sale = get_object_or_404(Sale, id=id)

    total = sale.quantity * sale.sale_price
    gst = total * Decimal("0.18")
    cgst = total * Decimal("0.09")
    sgst = total * Decimal("0.09")
    grand_total = total + gst

    customer_name = sale.customer.name if sale.customer else "Walk-in Customer"

    qr_code = generate_qr(sale.invoice_no, customer_name, sale.product.name, grand_total)
    barcode_url = generate_barcode(sale.invoice_no)

    context = {
        "sale": sale,
        "total": total,
        "gst": gst,
        "cgst": cgst,
        "sgst": sgst,
        "grand_total": grand_total,
        "qr_code": qr_code,
        "customer_name": customer_name,
        "barcode_url": barcode_url,
    }

    return render(request, "sales/invoice.html", context)


@login_required
def download_invoice(request, id):
    if not is_authorized(request.user):
        return HttpResponse("Access Denied")

    sale = get_object_or_404(Sale, id=id)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = (
        f'attachment; filename="Invoice_{sale.invoice_no}.pdf"'
    )

    pdf = canvas.Canvas(response)

    total = sale.quantity * sale.sale_price
    gst = total * Decimal("0.18")
    cgst = total * Decimal("0.09")
    sgst = total * Decimal("0.09")
    grand_total = total + gst

    customer_name = sale.customer.name if sale.customer else "Walk-in Customer"

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(180, 800, "SALES INVOICE")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 750, f"Invoice No : {sale.invoice_no}")
    pdf.drawString(50, 730, f"Customer   : {customer_name}")
    pdf.drawString(50, 710, f"Product    : {sale.product.name}")
    pdf.drawString(50, 690, f"Quantity   : {sale.quantity}")
    pdf.drawString(50, 670, f"Price      : Rs.{sale.sale_price}")
    pdf.drawString(50, 650, f"Total      : Rs.{total}")
    pdf.drawString(50, 630, f"CGST (9%)  : Rs.{cgst}")
    pdf.drawString(50, 610, f"SGST (9%)  : Rs.{sgst}")
    pdf.drawString(50, 590, f"GST (18%)  : Rs.{gst}")
    pdf.drawString(50, 570, f"Grand Total: Rs.{grand_total}")

    pdf.save()

    return response


@login_required
def send_invoice_email(request, id):
    sale = get_object_or_404(Sale, id=id)

    if not sale.customer or not sale.customer.email:
        return HttpResponse("Customer email not found.")

    customer_name = sale.customer.name if sale.customer else "Walk-in Customer"

    total = sale.quantity * sale.sale_price
    gst = total * Decimal("0.18")
    grand_total = total + gst

    subject = f"Invoice {sale.invoice_no}"

    message = f"""
Hello {customer_name},

Thank you for your purchase.

Invoice No : {sale.invoice_no}
Product    : {sale.product.name}
Quantity   : {sale.quantity}
Price      : Rs.{sale.sale_price}
Total      : Rs.{total}
GST (18%)  : Rs.{gst}
Grand Total: Rs.{grand_total}

Thank You.
"""

    email = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [sale.customer.email],
    )
    email.send()

    return HttpResponse("Invoice email sent successfully.")