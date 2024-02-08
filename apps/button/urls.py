from django.urls import include, path

from apps.button.api import (
    ButtonCreateApi,
    ButtonDetailApi,
    ButtonUpdateApi,
    ButtonListApi,
    ButtonListStatusApi
)

urlpatterns = [
    path(
        "get/",
        include(
            (
                [
                    path("<str:button_id>", ButtonDetailApi.as_view(), name="get_button_by_id"),
                    path("list/all", ButtonListApi.as_view(), name="list_button"),
                    path("list/status", ButtonListStatusApi.as_view(), name="list_status"),
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
                  path("<str:school_id>", ButtonCreateApi.as_view(), name="create_button"),
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