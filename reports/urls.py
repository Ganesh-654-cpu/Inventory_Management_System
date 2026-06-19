# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.report_home),
    
# ]


from django.urls import path
from .views import report_dashboard

urlpatterns = [
    path('', report_dashboard, name='reports'),
]