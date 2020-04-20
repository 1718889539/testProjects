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
        return Response({'status': 0, 'detail': 'success'})
