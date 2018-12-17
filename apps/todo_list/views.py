from rest_framework import viewsets
# 分页
from rest_framework.pagination import PageNumberPagination
# 过滤
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import *
from .serializers import *
from util import common_util


class ItemsPagination(PageNumberPagination):
    '''
    站点列表自定义分页
    '''
    # 默认每页显示的个数
    page_size = 8
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'


class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    pagination_class = ItemsPagination
    serializer_class = ItemsSerializer
    # 排序
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 搜索
    search_fields = ('title',)
