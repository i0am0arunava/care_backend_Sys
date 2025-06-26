from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CareLimitOffsetPagination(LimitOffsetPagination):
    max_limit = 200

    def get_paginated_response(self, data):
        return Response({"count": self.count, "results": data})
