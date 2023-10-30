from django.urls import path

from apps.users.api import UserListApi

urlpatterns = [path("", UserListApi.as_view(), name="list")]