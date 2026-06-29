
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from dashboard.views import dashboard

# urlpatterns = [
#     path('', dashboard, name='dashboard'),
#     path('admin/', admin.site.urls),
#     path('reports/', include('reports.urls')),
#       path("sales/", include("sales.urls"))
# ]

# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT
#     )


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from dashboard.views import dashboard

urlpatterns = [
    path("", include("accounts.urls")),
    path('', dashboard, name='dashboard'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),

    path('admin/', admin.site.urls),
    path('reports/', include('reports.urls')),
    path('sales/', include('sales.urls')),
   
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )