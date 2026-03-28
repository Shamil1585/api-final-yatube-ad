from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class ConditionalPagination(LimitOffsetPagination):
    """Возвращает список без пагинации, если нет limit/offset."""
    def paginate_queryset(self, queryset, request, view=None):
        has_limit = 'limit' in request.query_params
        has_offset = 'offset' in request.query_params
        if not has_limit and not has_offset:
            self.count = None
            return None
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        if self.count is None:
            return Response(data)
        return super().get_paginated_response(data)
