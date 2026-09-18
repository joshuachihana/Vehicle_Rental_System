from django.urls import path

from .views import (
    CustomerListCreateAPIView,
    CustomerDetailAPIView,
)


urlpatterns = [
    path(
        "customers/",
        CustomerListCreateAPIView.as_view(),
        name="customer-list-create",
    ),

    path(
        "customers/<int:pk>/",
        CustomerDetailAPIView.as_view(),
        name="customer-detail",
    ),
]