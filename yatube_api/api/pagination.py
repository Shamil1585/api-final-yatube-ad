from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CustomLimitOffsetPagination(LimitOffsetPagination):
    def get_paginated_response(self, data):
        # Проверяем, были ли переданы параметры limit или offset
        if not self.request.query_params.get('limit') and not self.request.query_params.get('offset'):
            # Если параметры не переданы, возвращаем просто список
            return Response(data)
        # Иначе возвращаем словарь с пагинацией
        return Response({
            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
