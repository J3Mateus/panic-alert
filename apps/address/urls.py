from django.urls import include, path

from apps.address.api import (
    AdressDetailApi,
    AddressCreateApi
)

urlpatterns = [
    path(
        "get/",
        include(
            (
                [
                    path("<str:cep>", AdressDetailApi.as_view(), name="get_address_by_cep"),
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
                  path("", AddressCreateApi.as_view(), name="create_address"),
                ],
                "create",
            )
        ),
    ),
]