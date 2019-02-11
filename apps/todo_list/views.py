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
    search_fields = ('title', 'content', 'date')
    ordering_fields = ('finish_flag', 'priority')
    ordering = ('finish_flag',)


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


def _get_degree(item):
    return getattr(common_util.df_config['DEGREE_MAP'], item.degree)


def _get_finish_degree(item):
    return getattr(common_util.df_config['DEGREE_MAP'], item.degree) * item.finish_degree


def _check_task_count():
    items = Items.objects.filter(date=date.today())
    if common_util.df_config['TASK_COUNT'] > items.count():
        return False
    return True


def _calc_rate():
    # 获取当天的所有items
    items = Items.objects.filter(date=date.today())
    # 按重要性分别对应3/2/1分，计算当天的总分
    total = sum(map(_get_degree, items))
    # 计算完成分
    achievement = sum(map(_get_finish_degree, items))
    # 按百分制计算当天的rate
    return common_util.floor(achievement / total)


class RateView(View):
    def get(self, request):
        ret = _check_task_count()
        if not ret:
            return common_util.json_response(False, message="当天任务数太少，不予评分")

        date = request.GET.get('date')
        ret = Schedule.objects.filter(date=date).values('rate')
        return common_util.json_response(True, data=ret[0])

    def post(self, request):
        ret = _check_task_count()
        if not ret:
            return common_util.json_response(False, message="当天任务数太少，不予评分")

        rate = _calc_rate()
        Schedule.objects.update_or_create(date=date.today(), defaults={"date": date.today(), "rate": rate})
        return common_util.json_response(True, message="更新评分成功")
