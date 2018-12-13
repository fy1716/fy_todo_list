from django.db import models
from django.contrib.auth.models import AbstractUser

from util import common_util


class UserProfile(AbstractUser):
    """
    用户信息
    """
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )
    # 用户用手机注册，所以姓名，生日和邮箱可以为空
    id = models.UUIDField(primary_key=True, default=common_util.df_uuid_hex, editable=False)
    name = models.CharField("姓名", max_length=30, null=True, blank=True)
    birthday = models.DateField("出生年月", null=True, blank=True)
    gender = models.CharField("性别", max_length=6, choices=GENDER_CHOICES, default="female")
    mobile = models.CharField("电话", max_length=11)
    email = models.EmailField("邮箱", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        # permissions = (
        #     ('add_userprofile', '新增用户信息'),
        #     ('change_userprofile', '修改用户信息'),
        #     ('delete_userprofile', '删除用户信息'),
        # )

    def __str__(self):
        return self.username
