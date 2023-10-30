from django.urls import include, path

from apps.school.api import (
    SchoolDetailApi,
    SchoolCreateApi,
    SchoolListApi,
    SchoolUpdateApi,
    SchoolDeleteApi
)


urlpatterns = [
    path(
        "get/",
        include(
            (
                [
                    path("<str:school_id>", SchoolDetailApi.as_view(), name="school_by_id"),
                    path("list/all", SchoolListApi.as_view(), name="list_school"),
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
                  path("", SchoolCreateApi.as_view(), name="create_school"),
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
                  path("<str:school_id>", SchoolUpdateApi.as_view(), name="update_school"),
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
                  path("<str:school_id>", SchoolDeleteApi.as_view(), name="update_school"),
                ],
                "delete",
            )
        ),
    ),
]