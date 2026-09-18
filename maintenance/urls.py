from django.urls import path

from .views import (
    MaintenanceListCreateAPIView,
    MaintenanceDetailAPIView,
)


urlpatterns = [
    path(
        "maintenance/",
        MaintenanceListCreateAPIView.as_view(),
        name="maintenance-list-create",
    ),

    path(
        "maintenance/<int:pk>/",
        MaintenanceDetailAPIView.as_view(),
        name="maintenance-detail",
    ),
]