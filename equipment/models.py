from django.db import models
from django.contrib.auth.models import User
from adminpro.utils.common import upload_direct_path


# Create your models here.

class EquipmentList(models.Model):
    status_list = (
        ('normal service', '正常使用'),
        ('out of service', '停用'),
        ('degradation', '降级使用'),
        ('in repairing', '故障待修'),
        ('scrapped', '报废'),
        ('others', '其他'),
    )
    name = models.CharField(u"设备名称", max_length=64, blank=True, null=True)
    location = models.CharField(u'分地点代码', max_length=12, null=True, blank=True, )
    lab_sn = models.CharField(u"设备编号", max_length=24, blank=True, null=True, unique=True)
    model = models.CharField(max_length=64, blank=True, null=True, verbose_name='型号')
    manufacturer = models.CharField(u"生产厂家", max_length=64, blank=True, null=True)
    manufacturer_sn = models.CharField(u"出厂编号", max_length=32, blank=True, null=True)
    first_duty = models.ForeignKey(User, null=True, blank=True, verbose_name="设备员", related_name="equipment_first",
                                   on_delete=models.SET_NULL)
    measure_range = models.CharField(max_length=128, null=True, blank=True, verbose_name="测量范围")
    status = models.CharField(choices=status_list, default="normal service", max_length=16, verbose_name='设备状态')
    purchased_date = models.DateField(null=True, blank=True, verbose_name="购买日期")
    remark = models.CharField(u"备注", max_length=64, null=True, blank=True)
    price = models.FloatField(null=True, blank=True, verbose_name="采购价格")
    asset_acq_way = models.CharField(verbose_name="资产取得方式", max_length=12, default="自有",
                                     choices=(("自有", "自有"),
                                            ("租赁", "租赁"), ))
    power = models.SmallIntegerField(null=True, blank=True, verbose_name="功率(w)")
    validation = models.FileField(upload_to='equipment/validation/', null=True, blank=True, verbose_name='验收资料上传')
    category = models.CharField(max_length=12, choices=(('关键设备', '关键设备'),
                                                        ('辅助设备', '辅助设备'),
                                                        ('计量器具', '计量器具'),), default='关键设备', verbose_name='分类')
    picture = models.ImageField(upload_to=upload_direct_path,
                                verbose_name='设备图片', max_length=128, blank=True, null=True, )

    def __str__(self):
        return "%s:%s(型号:%s)" % (self.lab_sn, self.name, self.model,)

    class Meta:
        verbose_name = "设备总表"
        verbose_name_plural = verbose_name
        db_table = "equipment_list"



