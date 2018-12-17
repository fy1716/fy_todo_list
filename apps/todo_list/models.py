from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=32, verbose_name="名称")
    degree = models.SmallIntegerField(verbose_name="重要度")


class Schedule(models.Model):
    date = models.DateField(verbose_name="日期")


class Items(models.Model):
    title = models.CharField(max_length=128, verbose_name="标题")
    content = models.CharField(max_length=1024, verbose_name="内容")
    start_time = models.TimeField(verbose_name="开始时间")
    period = models.SmallIntegerField(verbose_name="持续时长")
    finish_flag = models.BooleanField(verbose_name="是否完成", default=False)
    finish_degree = models.SmallIntegerField(verbose_name="完成度", default=0)  # 百分制
    priority = models.SmallIntegerField(verbose_name="优先级", default=0)
    item_type = models.ForeignKey('Type', on_delete=models.CASCADE, related_name='items')
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE)
    remark = models.CharField(max_length=512)
