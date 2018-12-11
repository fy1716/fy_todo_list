from django.db import models
from util import common_util
from DjangoUeditor import models as django_model


class Station(models.Model):
    id = models.UUIDField(primary_key=True, default=common_util.df_uuid_hex, editable=False)
    name = models.CharField(max_length=64, verbose_name="名称")
    address = models.CharField(max_length=256)
    hot_line = models.CharField(max_length=16)
    remark = django_model.UEditorField(verbose_name=u"描述", imagePath="goods/images/", width=1000, height=300,
                                       filePath="goods/files/", default='')

    class Meta:
        db_table = 'station'
