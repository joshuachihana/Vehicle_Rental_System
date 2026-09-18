from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/", include("customers.urls")),
    path("api/", include("locations.urls")),
    path("api/", include("vehicles.urls")),
    path("api/", include("reservations.urls")),
    path("api/", include("rentals.urls")),
    path("api/", include("payments.urls")),
    path("api/", include("maintenance.urls")),
]