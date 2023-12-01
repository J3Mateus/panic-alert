from django.urls import include, path

from apps.button.api import (
    ButtonCreateApi,
    ButtonDetailApi
)

urlpatterns = [
    path(
        "get/",
        include(
            (
                [
                    path("<str:button_id>", ButtonDetailApi.as_view(), name="get_button_by_id"),
                ],
                "get",
            )
        ),
    ),
    path(
        "create/",
        include(
            (
                [
                  path("", ButtonCreateApi.as_view(), name="create_button"),
                ],
                "create",
            )
        ),
    ),
]