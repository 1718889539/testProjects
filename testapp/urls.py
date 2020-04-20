# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import *

urlpatterns = (
    url(r'^api/test$', TestAPIView.as_view(), name='api_test'),
)
