from django.urls import include, path

urlpatterns = [
    path("auth/", include(("apps.authentication.urls", "authentication"))),
    path("users/", include(("apps.users.urls", "users"))),
    path("school/", include(("apps.school.urls", "school"))),
]