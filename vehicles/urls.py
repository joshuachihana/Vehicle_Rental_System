from django.urls import path

from .views import (
    VehicleTypeListCreateAPIView,
    VehicleTypeDetailAPIView,
    VehicleListCreateAPIView,
    VehicleDetailAPIView,
)


urlpatterns = [
    path(
        "vehicle-types/",
        VehicleTypeListCreateAPIView.as_view(),
        name="vehicle-type-list-create",
    ),

    path(
        "vehicle-types/<int:pk>/",
        VehicleTypeDetailAPIView.as_view(),
        name="vehicle-type-detail",
    ),

    path(
        "vehicles/",
        VehicleListCreateAPIView.as_view(),
        name="vehicle-list-create",
    ),

    path(
        "vehicles/<int:pk>/",
        VehicleDetailAPIView.as_view(),
        name="vehicle-detail",
    ),
]