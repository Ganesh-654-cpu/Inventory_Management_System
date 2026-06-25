
# from django.urls import path
# from .views import dashboard,export_products_excel
# from.views import export_products_excel

# urlpatterns = [
#     path('', dashboard, name='dashboard'),
    
#     path(
#         'export-products/',
#         export_products_excel,
#         name='export_products',
        
#       )
      
#     path('export-pdf/',export_products_pdf,name='export_pdf'),
        
# ]



from django.urls import path
from .views import (
    dashboard,
    export_products_excel,
    export_products_pdf
)

urlpatterns = [
    path(
        '',
        dashboard,
        name='dashboard'
    ),

    path(
        'export-products/',
        export_products_excel,
        name='export_products',
    ),

    path(
        'export-pdf/',
        export_products_pdf,
        name='export_pdf',
    ),
]