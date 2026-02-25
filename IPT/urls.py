from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # 2. Main Clinic App (Web + API)
    # This includes all paths from clinicapp/urls.py
    path('', include('clinicapp.urls')),

    # 3. Optional: DRF Login for the Browsable API
    # This adds a "Log In" button to the API web interface
    path('api-auth/', include('rest_framework.urls')),
]