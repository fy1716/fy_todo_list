#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Time: 2018/12/11 8:53
__author__ = 'Peter.Fang'

import xadmin
from xadmin import views


# xadmin全局设置
class BaseSetting(object):
    # 添加主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 全局配置，后台管理标题和页脚
    site_title = "general_framework"
    site_footer = "https://www.yydfsk.site"
    # 菜单收缩
    menu_style = "accordion"


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
