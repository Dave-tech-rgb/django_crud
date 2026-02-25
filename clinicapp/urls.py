from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# Ensure this matches the ViewSet name in your views.py
router.register(r'api-appointments', views.AppointmentViewSet)

urlpatterns = [
    # Fixed: Added .as_view() to all Class-Based Views
    path('', views.AppointmentListView.as_view(), name='appointment_list'),
    path('new/', views.AppointmentCreateView.as_view(), name='appointment_create'),
    path('<int:pk>/edit/', views.AppointmentUpdateView.as_view(), name='appointment_update'),
    path('<int:pk>/delete/', views.AppointmentDeleteView.as_view(), name='appointment_delete'),
    
    # API Routes
    path('api/', include(router.urls)),
]