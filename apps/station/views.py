from rest_framework import viewsets
from rest_framework import permissions
# 分页
from rest_framework.pagination import PageNumberPagination
# 过滤
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Station
from .filters import StationFilter
from .serializers import StationSerializer
from util import common_util


class StationPagination(PageNumberPagination):
    '''
    站点列表自定义分页
    '''
    # 默认每页显示的个数
    page_size = 12
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100


class StationViewSet(viewsets.ModelViewSet):
    common_util.debug('this is a log')
    '''
    站点列表，分页，搜索，过滤，权限，排序
    '''
    queryset = Station.objects.all()
    # 分页
    pagination_class = StationPagination
    # 序列化
    serializer_class = StationSerializer
    # 权限
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    # 排序
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 过滤
    filter_class = StationFilter
    # 搜索
    search_fields = ('name',)
    # 排序
    ordering_fields = ('id',)
