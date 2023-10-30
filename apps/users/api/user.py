from rest_framework.views import APIView


from apps.api.pagination import (
    LimitOffsetPagination,
    get_paginated_response,
)

from apps.api.mixins import ApiAuthMixin
from apps.users.selectors import user_list
from apps.users.serializers import OutputSerializer,FilterSerializer

class UserListApi(ApiAuthMixin,APIView):
    
    class Pagination(LimitOffsetPagination):
        default_limit = 20

    output_serializer = OutputSerializer
    filter_serializer = FilterSerializer
    
    def get(self, request):
        # Make sure the filters are valid, if passed
        filters_serializer = self.filter_serializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        users = user_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.output_serializer,
            queryset=users,
            request=request,
            view=self,
        )
