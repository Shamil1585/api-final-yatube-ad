from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CustomLimitOffsetPagination(LimitOffsetPagination):
    def get_paginated_response(self, data):
        # Если нет параметров limit и offset, возвращаем просто список
        if self.limit is None and self.offset is None:
            return Response(data)
        # Иначе возвращаем словарь с пагинацией
        return Response({
            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
