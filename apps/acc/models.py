from django.db import models


class Acc(models.Model):
    name = models.CharField(max_length=100, verbose_name='名称')
    acc_id = models.CharField(max_length=50, verbose_name='件号', unique=True)
    acc_type = models.CharField(max_length=30, verbose_name='类型')
    amount = models.PositiveSmallIntegerField(verbose_name='数量')
    cost = models.FloatField(verbose_name='成本')

    class Meta:
        db_table = 'acc'


class UserAcc(models.Model):
    station = models.ForeignKey('station.Station', on_delete=models.CASCADE, related_name='useracc')
    acc = models.ForeignKey('Acc', on_delete=models.CASCADE, related_name='useracc')
    common_name = models.CharField(max_length=50, verbose_name='常用名')
    storage_location = models.CharField(max_length=30, verbose_name='存储位置')
    price = models.PositiveSmallIntegerField(verbose_name='售价', null=True)
    low = models.PositiveSmallIntegerField(verbose_name='库存下限', null=True)
    high = models.PositiveSmallIntegerField(verbose_name='库存上限', null=True)
    remark = models.CharField(max_length=100, verbose_name='备注')

    class Meta:
        db_table = 'userAcc'
