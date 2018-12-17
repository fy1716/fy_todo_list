"""fy_todo_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import obtain_jwt_token
from .router import router
from util import common_util

schema_view = get_swagger_view(title=common_util.df_config['PLATFORM_NAME'])
urlpatterns = [
    path('front', TemplateView.as_view(template_name="index.html")),
    re_path('^', include(router.urls)),  # api路由
    path('admin/', admin.site.urls),  # xadmin后台
    path('xadmin/', xadmin.site.urls),  # xadmin后台
    path('ueditor/', include('DjangoUeditor.urls')),  # 富编辑
    # path('docs/', schema_view),  # swagger文档
    path('docs/', include_docs_urls(title=common_util.df_config['PLATFORM_NAME'])),  # rest文档
    path('api-auth', include('rest_framework.urls', namespace="rest_framework")),  # 认证
    path('jwt-auth/', obtain_jwt_token),
]
