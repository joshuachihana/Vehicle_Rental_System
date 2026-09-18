from django.urls import path

from .views import (
    RentalListCreateAPIView,
    RentalDetailAPIView,
    VehicleInspectionListCreateAPIView,
    VehicleInspectionDetailAPIView,
)


urlpatterns = [
    path(
        "rentals/",
        RentalListCreateAPIView.as_view(),
        name="rental-list-create",
    ),

    path(
        "rentals/<int:pk>/",
        RentalDetailAPIView.as_view(),
        name="rental-detail",
    ),

    path(
        "inspections/",
        VehicleInspectionListCreateAPIView.as_view(),
        name="inspection-list-create",
    ),

    path(
        "inspections/<int:pk>/",
        VehicleInspectionDetailAPIView.as_view(),
        name="inspection-detail",
    ),
]