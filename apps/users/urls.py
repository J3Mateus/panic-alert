from django.urls import path,include

from apps.users.api import (
    UserListApi,
    UserCreateApi,
    UserDeleteApi,
    UserUpdateApi
)

urlpatterns = [
    path(
        "get/",
        include(
            (
                [
                    path("list/all", UserListApi.as_view(), name="list"),
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
                  path("", UserCreateApi.as_view(), name="create_user"),
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
                  path("<str:user_id>", UserUpdateApi.as_view(), name="update_user"),
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
                  path("<str:user_id>", UserDeleteApi.as_view(), name="delete_user"),
                ],
                "delete",
            )
        ),
    ),
]

