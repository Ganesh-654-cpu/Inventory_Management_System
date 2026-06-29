from django.urls import path
from . import views

urlpatterns = [
    path("", views.sale_list, name="sale_list"),
    path("invoice/<int:id>/", views.invoice, name="invoice"),
    path( "invoice/download/<int:id>/",views.download_invoice,name="download_invoice"),
    path( "invoice/email/<int:id>/",views.send_invoice_email,name="send_invoice_email"   
),
]