from django.urls import include, path

from apps.cop.api import (
    CopDetailApi,
    CopCreateApi,
    CopListApi,
    CopUpdateApi,
    CopDeleteApi
)


urlpatterns = [
    path(
        "get/",
        include(
            (
                [
                    path("<str:cop_id>", CopDetailApi.as_view(), name="cop_by_id"),
                    path("list/all", CopListApi.as_view(), name="list_cop"),
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
                  path("", CopCreateApi.as_view(), name="create_cop"),
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
                  path("<str:cop_id>", CopUpdateApi.as_view(), name="update_cop"),
                ],
                "update",
            )
        ),
    ),
    path(
        "delete/",
        include(
            (
                [
                  path("<str:cop_id>", CopDeleteApi.as_view(), name="update_cop"),
                ],
                "delete",
            )
        ),
    ),
]