# -*- coding: utf-8 -*-

from __future__ import unicode_literals

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

__auth__ = 'zed'


class TestAPIView(APIView):
    '''测试接口'''
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            return Response({'status': 0, 'detail': '已认证'})
        return Response({'status': 1, 'detail': '未认证'})
