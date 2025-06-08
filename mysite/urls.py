from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tienda.urls')),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('api/v1/', include('tienda.api_urls')),  
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider'))
]
