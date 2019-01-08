from datetime import date
from django.views.generic import View
from django.core import serializers
from rest_framework import viewsets
# 分页
from rest_framework.pagination import PageNumberPagination
# 过滤
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# 混合类
from rest_framework import mixins

from .models import Items, Type, Schedule
from .serializers import TypeSerializer, ItemsSerializer, ScheduleSerializer
from util import common_util


class ItemsPagination(PageNumberPagination):
    """
    站点列表自定义分页
    """
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
    search_fields = ('title', 'content')
    ordering_fields = ('priority',)


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


def _calc_rate():
    return 100
    # 获取当天的所有items
    # 按重要性分别对应3/2/1分，计算当天的总分
    # 计算完成分
    # 按百分制计算当天的rate


class RateView(View):
    def get(self, request):
        date = request.GET.get('date')
        ret = Schedule.objects.filter(date=date).values('rate')
        return common_util.json_response(True, data=ret[0])

    def post(self, request):
        rate = _calc_rate()
        Schedule.objects.update_or_create(date=date.today(), rate=rate)
        return common_util.json_response(True)
