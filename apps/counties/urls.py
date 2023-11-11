from django.urls import include, path

from apps.counties.api import (
    CountieDetailApi,
    CountieListApi
)

urlpatterns = [
    path(
        "get/",
        include(
            (
                [
                    path("<str:countie_id>", CountieDetailApi.as_view(), name="countie_by_id"),
                    path("list/all", CountieListApi.as_view(), name="list_countie"),
                ],
                "get",
            )
        ),
    ),
]