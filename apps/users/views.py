# 视图
from rest_framework import viewsets
# 权限
from rest_framework import permissions
# 分页
from rest_framework.pagination import PageNumberPagination
# 过滤
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .serializers import UserSerializer
# 导入模型
from django.contrib.auth import get_user_model

User = get_user_model()


class UserPagination(PageNumberPagination):
    '''
    用户列表自定义分页
    '''
    # 默认每页显示的个数
    page_size = 10
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('id',)
