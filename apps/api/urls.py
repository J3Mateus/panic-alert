from django.urls import include, path

urlpatterns = [
    path("auth/", include(("apps.authentication.urls", "authentication"))),
    path("users/", include(("apps.users.urls", "users"))),
    path("school/", include(("apps.school.urls", "school"))),
    path("role/", include(("apps.role.urls", "role"))),
    path("cop/", include(("apps.cop.urls", "cop"))),
    path("counties/", include(("apps.counties.urls", "counties"))),
    path("address/", include(("apps.address.urls", "address"))),
]