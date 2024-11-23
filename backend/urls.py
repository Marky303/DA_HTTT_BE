from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Djoser authentication endpoints
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    
    # Account related endpoints
    path('account/', include('account.api.urls')),
    
    # Sales related endpoints
    path('sales/', include('sales.api.urls')),
    
    # Analysis related endpoint
    path('analysis/', include('analysis.api.urls')),
    
    # Dashboard related endpoint
    path('dashboard/', include('dashboard.api.urls')),
]
