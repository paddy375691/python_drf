from rest_framework import pagination
from rest_framework.response import Response
from collections import OrderedDict


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_query_param = "page_num"
    page_size_query_param = "page_size"
    max_page_size = 50

    def get_paginated_response(self, data):
        rsp = OrderedDict({
            'code': 200,
            'msg': '成功',
            'count': self.page.paginator.count,
            'data': data
        })
        return Response(rsp)
