"""fy_general_framework URL Configuration

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
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
from .router import router
from util import common_util

urlpatterns = [
    re_path('^', include(router.urls)),  # api路由
    path('xadmin/', xadmin.site.urls),  # xadmin后台
    path('ueditor/', include('DjangoUeditor.urls')),  # 富编辑
    path('docs/', include_docs_urls(title=common_util.df_config['PLATFORM_NAME'])),  # 文档
    path('api-auth', include('rest_framework.urls', namespace="rest_framework")),  # 认证
]
