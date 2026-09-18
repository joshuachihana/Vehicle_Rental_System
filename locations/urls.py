from django.urls import path

from .views import (
    LocationListCreateAPIView,
    LocationDetailAPIView,
)


urlpatterns = [
    path(
        "locations/",
        LocationListCreateAPIView.as_view(),
        name="location-list-create",
    ),

    path(
        "locations/<int:pk>/",
        LocationDetailAPIView.as_view(),
        name="location-detail",
    ),
]