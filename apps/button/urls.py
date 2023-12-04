from django.urls import include, path

from apps.button.api import (
    ButtonCreateApi,
    ButtonDetailApi,
    ButtonUpdateApi,
    ButtonListApi,
)

urlpatterns = [
    path(
        "get/",
        include(
            (
                [
                    path("<str:button_id>", ButtonDetailApi.as_view(), name="get_button_by_id"),
                    path("list/all", ButtonListApi.as_view(), name="list_button"),
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
    path(
        "update/",
        include(
            (
                [
                  path("<str:button_id>", ButtonUpdateApi.as_view(), name="update_button"),
                ],
                "update",
            )
        ),
    ),
]