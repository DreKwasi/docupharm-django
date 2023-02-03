from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("auth.api.urls")),
    path("api/accounts", include("accounts.api.urls")),
    path("api/interventions", include("interventions.api.urls"))
    
]
