from django.urls import include, path

from apps.type_incident.api import (
   TypeIncidentListApi,
)


urlpatterns = [
    path(
        "get/",
        include(
            (
                [
                    path("list/all", TypeIncidentListApi.as_view(), name="list_type_incident"),
                ],
                "get",
            )
        ),
    ),
]